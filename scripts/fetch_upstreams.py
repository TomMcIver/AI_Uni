#!/usr/bin/env python3
"""Fetch/status research upstreams without modifying dirty local clones."""
import argparse
import datetime as dt
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "research" / "upstream-manifest.json"
UPSTREAMS = ROOT / "research" / "upstreams"
LOCK = ROOT / "research" / "upstream-lock.json"

def run(args, cwd=None):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scope", choices=["core", "all"], default="core")
    op = p.add_mutually_exclusive_group(required=True)
    op.add_argument("--status", action="store_true")
    op.add_argument("--update", action="store_true")
    a = p.parse_args()
    rows = json.loads(MANIFEST.read_text(encoding="utf-8"))["repositories"]
    rows = [r for r in rows if a.scope == "all" or r["category"] == "core"]
    UPSTREAMS.mkdir(parents=True, exist_ok=True)
    inventory = json.loads(LOCK.read_text(encoding="utf-8")) if LOCK.exists() else {"schema_version": 1, "repositories": {}}
    failed = 0
    for repo in rows:
        path = UPSTREAMS / repo["directory"]
        if not path.exists():
            if a.status:
                print(f"MISSING {repo['name']}: {path}")
                inventory["repositories"][repo["name"]] = {"name": repo["name"], "url": repo["url"], "status": "not-cloned", "commit": None, "retrieved_at": None}
                continue
            # Partial clone avoids blob transfer until a file is inspected.
            result = run(["git", "clone", "--depth", "1", "--filter=blob:none", "--no-recurse-submodules", repo["url"], str(path)])
            if result.returncode:
                message = result.stderr.strip() or result.stdout.strip() or "clone failed"
                print(f"FAILED {repo['name']}: {message}"); failed += 1
                inventory["repositories"][repo["name"]] = {"name": repo["name"], "url": repo["url"], "status": "fetch-failed", "commit": None, "error": message, "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat()}
                continue
        elif not (path / ".git").exists():
            print(f"REFUSED {repo['name']}: destination exists but is not a git clone"); failed += 1; continue
        elif run(["git", "rev-parse", "--git-dir"], path).returncode:
            print(f"REFUSED {repo['name']}: incomplete or invalid git metadata; inspect manually before retry"); failed += 1; continue
        dirty = run(["git", "status", "--porcelain"], path)
        if dirty.returncode or dirty.stdout.strip():
            print(f"DIRTY {repo['name']}: preserving local changes; not updating"); failed += 1; continue
        if a.update and (path / ".git").exists():
            result = run(["git", "fetch", "--depth", "1", "--filter=blob:none", "origin"], path)
            if result.returncode:
                print(f"FAILED fetch {repo['name']}: {result.stderr.strip()}"); failed += 1; continue
            upstream = run(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], path)
            if upstream.returncode:
                print(f"REFUSED update {repo['name']}: no configured upstream branch; preserving checkout"); failed += 1; continue
            result = run(["git", "merge", "--ff-only", upstream.stdout.strip()], path)
            if result.returncode:
                print(f"FAILED update {repo['name']}: {result.stderr.strip()}"); failed += 1; continue
        sha = run(["git", "rev-parse", "HEAD"], path).stdout.strip()
        branch = run(["git", "branch", "--show-current"], path).stdout.strip()
        remote = run(["git", "remote", "get-url", "origin"], path).stdout.strip()
        date = run(["git", "show", "-s", "--format=%cI", "HEAD"], path).stdout.strip()
        lic = [x.name for x in path.iterdir() if x.is_file() and x.name.lower().startswith(("license", "copying"))]
        entry = {"name": repo["name"], "url": remote or repo["url"], "commit": sha, "branch": branch or "detached", "commit_date": date, "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(), "license_files": lic, "status": "fetched; source audit pending"}
        inventory["repositories"][repo["name"]] = entry
        print(f"OK {repo['name']} {sha} ({branch or 'detached'}) license-files={lic}")
    LOCK.write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
