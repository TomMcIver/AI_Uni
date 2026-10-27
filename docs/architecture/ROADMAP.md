# Development roadmap

This is a phased plan; no production capability is claimed.

| Milestone | Scope | Measurable exit criteria |
|---|---|---|
| M0 Research and foundation | Source audits, licences, decision, docs, standards, issues | Core candidate source and tests pinned/audited; ADR supported by evidence; backlog and local bootstrap validated |
| M1 Shared memory MVP | Persistence, project namespaces, events, Claude/Codex adapters, incremental sync, retrieval, provenance, validation | Future scenarios 1–10: bidirectional handover; incremental fetch; bounded fresh snapshot; conflict; recovery; permissions; provenance; measured token comparison; two providers independent |
| M2 Automatic sync and forum | Hooks, daemon, durable delivery, forum, manual sync, notifications, conflicts, inspection UI | Hook failure/restart/replay does not lose committed events; forum ACL and delivery/read semantics verified |
| M3 Unified chat/gateway | React UI, provider config, model selection, context, MCP, local inference, usage, users/history | At least two independent providers stream through UI; permission-scoped project context and token/cost records verified |
| M4 Orchestration | Registry, decomposition, model choice, isolated workers, DAG, reviews, approvals, budgets, scheduling | Repeatable task lifecycle with isolated execution, denied unauthorized actions, audit report and budget/approval tests |
| M5 Platform hardening | Multi-user auth, secrets, packaging, observability, backup, benchmarks, API, plugins, ops docs | Threat model gates pass; tested backup/delete/restore; measured performance targets set and met; deployment/recovery docs exercised |

## Future executable acceptance scenarios

1. Claude→Codex and 2. Codex→Claude recover changed files, decisions, completed work, open tasks and source references without user copying.
3. A cursor through N fetches only eligible new events plus requested targeted context.
4. Fresh client gets bounded snapshot and relevant updates.
5. Conflicting claims are surfaced, not silently overwritten.
6. Restart/uncertain response neither loses committed events nor duplicates applied effects.
7. Unauthorised client cannot access private user or unrelated project memory.
8. Important claims cite source evidence.
9. Actual input tokens compared with full-context baseline; no assumed savings.
10. Two model providers use the same memory/event contract without provider assumptions in core storage.
