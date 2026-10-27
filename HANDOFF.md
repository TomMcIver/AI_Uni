# AI_Uni handoff

## START HERE FOR NEXT AGENT

This repository is in **research/bootstrap**. First read [AGENTS.md](AGENTS.md), inspect `git status`, then review [architecture overview](docs/architecture/OVERVIEW.md), [fork decision](docs/research/FORK_DECISION.md), and `.github/issue-backlog/`. No application runtime exists. The next task is to get this bootstrap committed/reviewed, then complete the source and licence audit once network access is available; do not begin product implementation ahead of M0 evidence/Issues.

### State labels

- **DECIDED:** repository branch is `main`; project code licence is pending owner choice; clones are research-only and ignored; no hidden model reasoning transfer is claimed.
- **PROPOSED:** composition before fork; event/memory contract designs in `docs/architecture/`; OpenClaw is an evaluation candidate, not selected.
- **UNVERIFIED:** all candidate source-level architecture and licences; CLI hook/API completeness; all proposed schemas and integration assumptions.
- **BLOCKED:** network fetch failed at the configured proxy; `gh auth status` reports invalid tokens and `gh repo view` cannot reach API. Thus upstream revisions, real GitHub labels/milestones/issues, and board creation were not performed.
- **COMPLETED:** initial docs, manifest, fetch utility, threat baseline, issue backlog drafts and local publication helper are created (see files; validation state below).

## Project and user problem

The initial use case is a developer working in Claude Code, then Codex CLI (or vice versa), losing the other session's decisions, changed-file context, test results and open tasks. The project should capture accessible user-authorised events/artifacts, validate and scope knowledge, and deliver a small authoritative snapshot plus relevant unseen updates. The user must not repeat or manually copy context. This synchronizes verified knowledge and accessible artifacts, not hidden chain-of-thought or proprietary model session state.

## Product vision

One local-first, extensible, permission-aware intelligence system for multiple providers/models, agent CLIs/runtimes, persistent scoped memory, automatic/manual synchronization, agent messages/reviews/handoffs, memory inspection, optional unified chat/gateway, and later approval-gated orchestration. Memory scopes: user, project, session, agent, optional organisation/forum. Long-term hosted multi-user operation must preserve isolation and deletion.

## Current repository state

Initial Git commit: `8e28d5afc4cf7d2ef12e16736fa607f87d0dde47`; branch `main`; remote `https://github.com/TomMcIver/AI_Uni.git`. Work began on a clean tree with only README. No commit was made during this task. No product code, runtime, CI, test suite, licence, or application dependencies exist.

## Completed bootstrap work

- Replaced README with project/status/architecture/roadmap/contribution overview.
- Added agent rules and contributor guide.
- Added research manifest, ignore rules, clone/status/update utility.
- Added proposed architecture docs and ADR 0001.
- Added research inventory/comparison/audit/license/gap/decision docs.
- Added 39 local issue drafts (9 epics plus 30 scoped research/architecture/implementation tasks), templates, and idempotent publication helper.

## Upstreams and research findings

The catalog lists OpenClaw, Total Agent Memory, multiagents, Orchestra, Letta Code, OpenHands, software-agent-sdk, Hermes, Moyai, OpenCode, LibreChat, Open WebUI, Mem0, OpenMemory, Graphiti, LiteLLM and Codex. GitHub repo landing page searches confirm some repository descriptions exist, but **no pinned source commit was inspected**. One incomplete `research/upstreams/openmemory/.git` remains from an interrupted clone; remove or resume only after checking it's an unmodified partial clone. No successful repositories/revisions can currently be claimed. Current inventory: `docs/research/UPSTREAM_INVENTORY.md`.

Early public search snippets surfaced OpenClaw docs describing session/lifecycle events and per-connection WebSocket sequence metadata, plus Total Agent Memory and multiagents descriptions. Those are mutable documentation/marketing signals, not source verification and are not enough for a selection.

## Fork recommendation

Proposed composition-first, no permanent base selected. Own stable memory/event/cursor/permission contracts; evaluate OpenClaw as runtime integration, LiteLLM as gateway, and memory-specific systems as components. Reassess after pinned source/test/licence audit and a thin integration spike. Alternatives and scoring criteria: [fork decision](docs/research/FORK_DECISION.md). ADR 0001 is explicitly proposed.

## Proposed architecture and requirements

- **Memory:** scoped structured records, immutable evidence, version history, provenance, confidence/review state, validity intervals, contradictions, hybrid retrieval, permission-first filtering, bounded snapshots, token budgets, deletion and cross-project isolation. See [MEMORY](docs/architecture/MEMORY.md).
- **Events/sync:** append-only records, stable IDs, per-stream committed sequence, per-client scoped cursors, idempotent ingest/apply, replay, durable receipt/ack, snapshots/high-watermarks, conflict handling and revocation. Avoid relying on global offsets or timestamps as total order. See [EVENT_MODEL](docs/architecture/EVENT_MODEL.md).
- **CLI:** Claude Code and Codex first; actual supported hooks/transcript surfaces remain to be researched at implementation-time versions. Manual sync is needed where automatic hooks are absent. See [CLI integration](docs/architecture/CLI_INTEGRATION.md).
- **Forum:** typed messages, identity, recipient/topic, scope, source references, delivery/read states, threads/resolution; agent text is untrusted. See [communication](docs/architecture/AGENT_COMMUNICATION.md).
- **Gateway/chat:** React + TypeScript later; evaluate LiteLLM before duplicating provider routing. See [gateway](docs/architecture/MODEL_GATEWAY.md).
- **Orchestration:** later milestone; isolated workers, least privilege, separate read/write/execute/network/credential permissions, human approvals, cost limits and audit. See [security](docs/architecture/SECURITY.md).

## Decisions and unresolved questions

SQLite local vs PostgreSQL shared deployment strategy; API/auth model; cursor persistence/signing; client-specific hook/event coverage; chosen vector search; secrets/encryption model; data retention/deletion semantics; forum broker; UI component reuse; project licence; final base/composition boundaries. Resolve through research and ADRs, not silent assumptions.

## Risks and limitations

No source-level audits or licence review completed; no current-version product docs verified beyond initial public search; no executable service/tests; network clone blocked; GitHub credentials invalid. Existing partial clone must be handled carefully. User conversation data, repositories, and credentials demand strict minimisation, provenance, scope isolation, deletion, and execution sandboxing.

## GitHub roadmap and exact next tasks

Six milestones M0–M5 are defined in [ROADMAP](docs/architecture/ROADMAP.md). Offline drafts reside in `.github/issue-backlog/`; publication did not occur because CLI auth and network failed. Next recommended Issue: **M0 – Pin and source-audit the five core upstreams, with exact commit citations and tests**. Then verify licences and the actual Claude/Codex integration contracts. Publish drafts only after authenticating `gh` and checking duplicates.

## Commands and verification

Prerequisite: Git and Python 3.10+; on this machine `py -3` works. Intended commands:

```powershell
py -3 scripts/fetch_upstreams.py --scope core --update
py -3 scripts/fetch_upstreams.py --scope all --update
py -3 scripts/fetch_upstreams.py --scope all --status
py -3 scripts/publish_issues.py --dry-run
py -3 scripts/publish_issues.py
```

Actual checks on 2026-10-28: Python 3.14.8 compiled both scripts; manifest and issue JSON parsed; dry-run printed all 39 drafts; fetch `--status` correctly reported all 17 repositories not cloned; `git diff --check` passed. These are bootstrap checks only, not product tests. GitHub publication was not run because `gh auth status` reported invalid tokens and the API proxy refused connections. No project build/test exists.

## Relevant documents

[README](README.md) · [AGENTS](AGENTS.md) · [research inventory](docs/research/UPSTREAM_INVENTORY.md) · [comparison](docs/research/OPEN_SOURCE_COMPARISON.md) · [audit](docs/research/CODE_AUDIT.md) · [license](docs/research/LICENSE_REVIEW.md) · [feature gaps](docs/research/FEATURE_GAP_ANALYSIS.md) · [ADR](docs/adr/0001-composition-before-fork.md).

## Last completed work and verification

The bootstrap files were created on 2026-10-28. GitHub auth/API and upstream fetch were attempted and blocked; no upstreams/revisions, issues, labels, milestones, project board, source audit or license verification can be claimed. Python compilation, JSON parsing, publisher dry run, fetch status and `git diff --check` passed as noted above. The bootstrap changes are committed locally on `main` as `4b9c5c1` (`Bootstrap AI_Uni research and architecture`); push status is pending confirmation. The `.gitignore` and this handoff line are included in the finalized bootstrap commit.
