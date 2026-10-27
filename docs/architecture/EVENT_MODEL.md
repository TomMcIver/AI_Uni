# Event model and incremental synchronization

**Status: candidate contract.** Candidate attributes: `event_id`, `schema_version`, `tenant_id`, `project_id`, `session_id`, `actor_id`, `agent_id`, `event_type`, `stream_id`, `stream_sequence`, `occurred_at`, `ingested_at`, `source_reference`, `payload`, `content_hash`. Add producer/client identity, idempotency key, classification, and deletion metadata if required. Timestamps are descriptive; they do not establish a total distributed order.

## Ordering and identity

Use stable event IDs (producer idempotency key or deterministic scoped key) for deduplication. Allocate strictly increasing sequence values within a stream transactionally at commit. A stream can be tenant/project/session/agent scoped; define which streams a cursor covers. Do not use one global offset as the sole multi-tenant checkpoint. Cross-stream ordering is partial and should rely on causal references when needed.

## Ingestion/checkpoint protocol

1. Authenticate client and authorise the target scope.
2. Validate schema/version, size and source; insert event and idempotency mapping in one transaction.
3. Return durable event ID and committed stream sequence only after commit.
4. Client persists its local delivery state and retries with the same idempotency key after uncertain responses.
5. Client fetches from an opaque cursor bound to tenant, client, stream set and policy version. Server returns events plus next cursor; client applies idempotently, then explicitly acknowledges after durable local apply.
6. Acknowledgement cannot advance beyond delivered/committed records. Cursor expiry requires bounded snapshot plus replay, never silent gap acceptance.

The cursor token must be opaque/signed or server stored, access controlled, revocable, and distinct per client. Event ordering sequence and cursor token are separate concepts.

## Replay, schema, deletion and compaction

Keep schema version and pure upcasters; unknown incompatible events are quarantined, not dropped. Replay must preserve idempotence and provenance. Deletion/revocation is represented by authorised tombstone/control events and propagated to projections. Compaction emits a snapshot with a declared high-watermark and provenance coverage; retain audit/evidence according to policy. Never compact past unacknowledged clients without marking their cursors expired and requiring snapshot recovery.

## Failure cases

Test crash before commit, after commit before response, duplicate send, crash during apply, ack loss, event arrival after snapshot boundary, cursor revocation, permission change, schema migration, out-of-order timestamps, and restored backups. Use DB transaction isolation and outbox pattern if projections/notifications are asynchronous.
