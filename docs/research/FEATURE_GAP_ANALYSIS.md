# Feature gap analysis

Status values: **implemented and verified**, **implemented but not tested**, **partially supported**, **requires an adapter**, **requires modification**, **missing**, **unknown**. Since no upstream source checkout completed, candidate-specific implementation status is **unknown** unless clarified below.

| Capability | AI_Uni now | Candidate evidence / next work |
|---|---|---|
| Repository bootstrap docs/script | Implemented locally, verification pending | Run syntax and behavior checks |
| Durable cross-tool event store | Missing | Audit candidates and define contract |
| Scoped memory/provenance/versioning | Design proposed, unimplemented | Audit TAM, Letta, Mem0, Graphiti |
| Claude Code capture | Requires an adapter; unsupported here | Verify official hook/API limits and versioning |
| Codex capture | Requires an adapter; unsupported here | Verify official CLI/app-server events |
| Incremental per-client cursor/ack/replay | Design proposed, unimplemented | Inspect candidate event/reconcile paths |
| Snapshot/compaction/revocation | Design proposed, unimplemented | Define semantics and tests |
| Agent forum | Missing | Audit multiagents/Orchestra, then define ACL contract |
| Unified model gateway | Missing | Evaluate LiteLLM; avoid duplicate routing |
| Unified chat UI | Missing | Evaluate LibreChat/Open WebUI as components |
| Isolated orchestration | Missing/future | Audit OpenHands SDK, ACP, worktree/container patterns |
| Tenant/auth/permissions | Design baseline only | Must be implemented and security tested |
| Licensing clearance | Unknown/pending | Inspect full upstream licences and project owner decision |

No row should be upgraded based on README-only claims. Add source/test citations and an inspected commit for each candidate feature.
