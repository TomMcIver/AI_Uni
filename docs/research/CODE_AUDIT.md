# Source-level code audit

## Audit status

**Not completed.** Direct clone attempts could not complete in the execution environment (GitHub proxy endpoint refused connections). No commit SHA was inspected; no source file or test can honestly be cited as verified. Public repository landing pages and search results do not satisfy the requested source audit. `research/upstream-lock.json` must contain a revision before an audit is accepted.

## Required per-project evidence sheet

For OpenClaw, Total Agent Memory, multiagents, Orchestra, and Letta Code first; then additional repositories, capture:

| Dimension | Required evidence |
|---|---|
| Revision/licence | Commit-pinned tree, full licence/notices, contribution/dependency conditions |
| Language/runtime | manifests, lockfiles, toolchain and supported platforms |
| Entry/folders | executable entrypoints and module boundaries |
| Storage/session/events | schemas, migrations, write path, ordering, replay, cursor/ack behavior and tests |
| Memory | record formats, scope, provenance, versioning, extraction/retrieval, compaction/deletion |
| Model/provider | interface, streaming, credential handling, capability model |
| CLI/adapters | hooks/API/protocols, supported versions, failure/retry semantics |
| Collaboration | identity, message persistence, ACL, delivery/read semantics |
| Execution/security | sandboxing, auth, permission checks, network/credential access |
| Extensibility/API | supported plugin contract and stability |
| Tests/operations | coverage around critical flows, CI, deployment, observability, recovery |
| Maintenance | release cadence, contributor activity, breaking changes and bus factor |

Add a subsection per candidate with exact `https://github.com/<owner>/<repo>/blob/<sha>/<path>` links, line ranges where available, test references, and finding status: verified / partial / untested / unknown. Do not fill gaps with README prose.

## Audit focus

OpenClaw session reconciliation and external harness integration; TAM separation between core and AI layers, extraction and provenance; multiagents broker and ACL/license; Orchestra adapter/reconnect/worktree ownership; Letta memory blocks and local/hosted boundaries; OpenHands SDK ACP client/server. Audit design hypotheses from the original project brief against code and tests.
