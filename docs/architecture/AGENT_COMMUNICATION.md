# Agent communication

**Status: future capability.** Forum operations include send/list/reply, review request, task delegation/result, handover acknowledgement, resolve discussion, activity query, and project subscription. Message fields should include stable ID, sender identity, recipient/topic, scope, type, timestamps, source references, related task/Issue, delivery/read state, thread, and resolution state.

Messages are untrusted data. A message cannot grant permissions, override policy, execute code, or alter a decision merely by asserting authority. Validate sender identity and current scope on every read/write; prevent spoofing and replay with authenticated identities, nonces/idempotency, and audit events. Separate delivery from read/ack state. Conflicts stay visible and unresolved until an authorised actor resolves them.

Initial broker selection is open; compare relational transactional outbox with lightweight local SQLite queue for local-first operation. Do not introduce a standalone broker until measured needs require it.
