# ADR 0001: Compose before forking a platform

- Status: Proposed pending upstream source audit
- Date: 2026-10-28

## Context

AI_Uni needs durable cross-client memory and event synchronization, but no audited candidate has yet been cloned in this environment. The stated product needs tool interoperability, scoped memory, per-client cursors, permissions, and eventual provider/agent choice. A large application fork creates upstream merge and licensing costs before proving its boundaries fit.

## Decision

Start with composition: define AI_Uni-owned event, memory, cursor and permission contracts; integrate mature gateways or agent runtimes through supported APIs/adapters. Keep OpenClaw as a serious candidate for selective integration, not the selected base. Do not copy upstream code until a separate licence and maintenance review supports it.

## Alternatives

- Fork OpenClaw now: broad runtime/gateway functionality, but source compatibility and licensing/maintenance implications remain unverified here.
- Build everything in-house: maximum control, duplicates mature provider and runtime work.
- Adopt a memory-only project: potentially useful subsystem, but does not alone solve event ordering, client adapters, forum, or UI.

## Consequences

AI_Uni must define stable contracts and adapter boundaries early. Re-evaluate after source audit and a thin integration spike. This is a reversible bootstrap recommendation, not a permanent foundation selection.

## Evidence and review trigger

See `docs/research/FORK_DECISION.md`, `CODE_AUDIT.md`, and `LICENSE_REVIEW.md`. Revisit after core repositories are cloned at recorded commits and their relevant modules/tests are inspected.
