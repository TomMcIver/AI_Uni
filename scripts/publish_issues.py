#!/usr/bin/env python3
"""Publish local issue drafts via gh; skips exact titles already present."""
import argparse, json, pathlib, subprocess, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
DRAFTS=ROOT/".github"/"issue-backlog"/"issues.json"
INDEX=ROOT/".github"/"issue-backlog"/"published-index.json"
MILESTONES=["M0: Research and repository foundation","M1: Shared memory MVP","M2: Automatic sync and agent forum","M3: Unified chat and model gateway","M4: Agent orchestration","M5: Platform hardening"]
LABELS=["type:research","type:feature","type:bug","type:architecture","type:documentation","type:security","type:testing","type:infrastructure","type:epic","priority:P0","priority:P1","priority:P2","priority:P3","area:gateway","area:memory","area:sync","area:cli","area:agents","area:ui","area:security","area:research","area:infrastructure"]
def gh(args,check=True):
 r=subprocess.run(["gh",*args],text=True,capture_output=True)
 if check and r.returncode: raise RuntimeError(r.stderr.strip() or r.stdout.strip())
 return r
def main():
 p=argparse.ArgumentParser(); p.add_argument("--dry-run",action="store_true"); a=p.parse_args()
 drafts=json.loads(DRAFTS.read_text(encoding="utf-8"))
 if a.dry_run:
  for x in drafts: print(x["title"])
  print(f"{len(drafts)} drafts; no changes made"); return 0
 status=gh(["auth","status"],False)
 if status.returncode: print(status.stderr); return 2
 repo=gh(["repo","view","--json","nameWithOwner","-q",".nameWithOwner"]).stdout.strip()
 existing=json.loads(gh(["issue","list","--repo",repo,"--state","all","--limit","1000","--json","number,title,url"]).stdout)
 bytitle={i["title"].casefold():i for i in existing}; index=json.loads(INDEX.read_text(encoding="utf-8")) if INDEX.exists() else {"repository":repo,"issues":[]}
 existing_labels=json.loads(gh(["label","list","--repo",repo,"--limit","1000","--json","name"]).stdout)
 known_labels={x["name"] for x in existing_labels}
 for label in LABELS:
  if label not in known_labels: gh(["label","create",label,"--repo",repo])
 for title in MILESTONES:
  found=gh(["api",f"repos/{repo}/milestones","--paginate"],False)
  try: ms=json.loads(found.stdout)
  except Exception: ms=[]
  if not any(m.get("title")==title for m in ms):
   gh(["api",f"repos/{repo}/milestones","-f",f"title={title}"],False)
 for x in drafts:
  body=("## Objective\n"+x["objective"]+"\n\n## Background\n"+x["background"]+"\n\n## Technical approach\n"+x["approach"]+"\n\n## Scope\n"+x["scope"]+"\n\n## Out of scope\n"+x["out"]+"\n\n## Dependencies\n"+("\n".join("- "+d for d in x["deps"]) or "None")+"\n\n## Acceptance criteria\n- "+x["criteria"]+"\n\n## Test requirements\n"+x["tests"]+"\n\n## Relevant files or research\n"+x["files"]+"\n\n## Priority\n"+x["priority"]+"\n\n## Milestone\n"+x["milestone"])
  if x["title"].casefold() in bytitle: item=bytitle[x["title"].casefold()]
  else:
   cmd=["issue","create","--repo",repo,"--title",x["title"],"--body",body,"--milestone",x["milestone"]]
   for label in x["labels"]: cmd += ["--label",label]
   url=gh(cmd).stdout.strip(); item={"title":x["title"],"url":url,"number":int(url.rstrip("/").split("/")[-1])}
  if not any(y.get("title")==item["title"] for y in index["issues"]): index["issues"].append(item)
  INDEX.write_text(json.dumps(index,indent=2)+"\n",encoding="utf-8"); print(item.get("number"),item["title"],item.get("url",""))
 return 0
if __name__=="__main__":
 try: sys.exit(main())
 except Exception as e: print(f"ERROR: {e}",file=sys.stderr); sys.exit(1)
