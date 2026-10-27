# Upstream inventory

## Scope and retrieval state

The canonical catalog is [`research/upstream-manifest.json`](../../research/upstream-manifest.json); the fetch utility is [`scripts/fetch_upstreams.py`](../../scripts/fetch_upstreams.py). It creates shallow, blob-filtered clones without submodules or install scripts, records inspected revisions in `research/upstream-lock.json`, and refuses dirty repositories before update. `research/upstreams/` is ignored. Use `py -3 scripts/fetch_upstreams.py --scope core --update`, then `--scope all --update`; `--status` is read-only apart from inventory refresh.

Initial fetch was attempted on 2026-10-28. The environment's GitHub API reported proxy connection refusal (`127.0.0.1:9`); the fetch invocation did not produce a complete set of clones or a trustworthy lock inventory. One partial `openmemory/.git` directory was left by the interrupted attempt, with no inspected commit. Treat all listed repositories as **not source-audited** until successful fetch and lock entries exist. Do not count current working documentation or public search snippets as source inspection.

| Candidate | Category | Repository | State |
|---|---|---|---|
| OpenClaw | Core | [openclaw/openclaw](https://github.com/openclaw/openclaw) | Fetch blocked; source audit pending |
| Total Agent Memory | Core | [vbcherepanov/total-agent-memory](https://github.com/vbcherepanov/total-agent-memory) | Fetch blocked; source audit pending |
| multiagents | Core | [zetbrush/multiagents](https://github.com/zetbrush/multiagents) | Fetch blocked; source audit pending |
| Orchestra | Core | [theorchestradev/orchestra](https://github.com/theorchestradev/orchestra) | Fetch blocked; source audit pending |
| Letta Code | Core | [letta-ai/letta-code](https://github.com/letta-ai/letta-code) | Fetch blocked; source audit pending |
| OpenHands | Additional | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Fetch blocked; audit pending |
| Software Agent SDK | Additional | [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) | Fetch blocked; audit pending |
| Hermes Agent | Additional | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Fetch blocked; audit pending |
| Moyai | Additional | [BerriAI/moyai](https://github.com/BerriAI/moyai) | Fetch blocked; audit pending |
| OpenCode | Additional | [anomalyco/opencode](https://github.com/anomalyco/opencode) | Fetch blocked; audit pending |
| LibreChat | Additional | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | Fetch blocked; audit pending |
| Open WebUI | Additional | [open-webui/open-webui](https://github.com/open-webui/open-webui) | Fetch blocked; audit pending |
| Mem0 | Infrastructure | [mem0ai/mem0](https://github.com/mem0ai/mem0) | Fetch blocked; audit pending |
| OpenMemory | Infrastructure | [mem0ai/openmemory](https://github.com/mem0ai/openmemory) | Partial `.git` only; no commit verified |
| Graphiti | Infrastructure | [getzep/graphiti](https://github.com/getzep/graphiti) | Fetch blocked; audit pending |
| LiteLLM | Infrastructure | [BerriAI/litellm](https://github.com/BerriAI/litellm) | Fetch blocked; audit pending |
| Codex | Infrastructure/client | [openai/codex](https://github.com/openai/codex) | Fetch blocked; audit pending |

## Next audit procedure

Run fetch on a network-enabled environment. Record SHA/branch/date/remote and licence filenames. Inspect manifests, entry points, storage schemas, core source modules, API boundaries and relevant tests at that SHA. Add exact `blob/<sha>/path` references to `CODE_AUDIT.md`. Licence filename discovery is not legal review: inspect the full licence, notices, dependencies, assets and distribution conditions.
