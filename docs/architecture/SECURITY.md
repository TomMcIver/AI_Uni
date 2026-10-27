# Security and privacy

**Status: threat model baseline.** Data includes private conversations, repository references, credentials and tool outputs. Default deny; least privilege; local-first does not mean automatically safe.

| Threat | Required control |
|---|---|
| Prompt injection in forum/memory/tool output | Treat as untrusted content; isolate data from policy; no privilege conveyed by text |
| Malicious MCP server / external result | Explicit capability allowlist, provenance, timeouts, output validation, sandbox |
| Cross-project/tenant leakage | Authorise before retrieval/ranking; scoped keys; isolation tests |
| Credential exposure | OS secret store or dedicated vault; redact logs; never memory/event payload |
| Privilege escalation / arbitrary execution | Separate read/write/execute/network/credential permissions; approval gates; restricted workers |
| Agent impersonation / replay | Authenticated identities, signed or protected cursors, idempotency, expiry, audit |
| Memory poisoning / stale authority | Provenance, validation, confidence/review state, versioning, contradiction surfacing |
| Stale permission / deletion failure | Re-check on each operation; revocation/deletion tombstones through indexes, snapshots and backups |
| Untrusted upstream source | Research-only clones, no install scripts, inspect pinned revision/licence, isolate execution |

No autonomous worker gets unrestricted host access by default. Permissions distinguish read, write, execute, network, credential access and approvals. Tool output/model success is never security validation. Design for export/deletion, retention controls, backup deletion watermarks, and minimised logging. Before hosted multi-user use, conduct a security review and incident/recovery exercise.
