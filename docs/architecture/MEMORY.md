# Memory architecture

**Status: design proposal.** Memory is a set of scoped, versioned records with evidence; it is not a mutable all-project prompt file. Candidate scopes: user, organisation, project, session, agent, forum/thread. Each read is authorised against tenant/project/actor before retrieval.

Candidate record fields: stable `memory_id`, scope and scope ID, kind, content, source event/reference, author/actor, created/updated timestamps, validity interval, confidence, review state, version/parent version, content hash, sensitivity/retention class, and deletion/tombstone state. Schema is not final.

## Behaviour

- Keep immutable evidence/events separately from derived claims. A correction creates a version and relation; it does not erase provenance.
- Preserve contradictory claims as explicit competing assertions with sources and time intervals. Do not resolve by last writer without policy or human review.
- Store provenance at claim level. Distinguish explicit user confirmation, observed artifact, tool output, and model inference.
- Validate extracted claims for scope, source reachability, schema, sensitivity, and permission before promotion. Low confidence/inferred updates can remain pending review.
- Support keyword plus vector retrieval; filter by permissions first, then rank. Include citations and validity in output.
- Build bounded authoritative snapshots from accepted current records; append deltas since a per-client checkpoint. Retrieve older relevant evidence on demand.
- Apply token budgets with measured counts. Never promise incremental retrieval always saves tokens.
- Deletion/revocation must propagate to derived indexes, snapshots, caches and exports, subject to documented retention/legal policy. Tombstones prevent resurrection during replay.
- Support human inspection, editing, dispute resolution, export and deletion.

## Isolation and lifecycle

Cross-project retrieval is opt-in and permission checked. User memory is not implicitly copied into every tenant/project. Agent/session memories expire or compact under explicit retention policy; source evidence and derived summaries have distinct retention. Backup restoration must respect deletion watermarks.

## Open questions

SQLite/Postgres migration shape; vector backend; encryption-at-rest/key ownership; retention defaults; confidence calibration; organisational sharing and roles. Resolve with ADRs before implementation.
