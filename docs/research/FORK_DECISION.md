# Fork/composition decision

## Recommendation

**Proposed: composition first; no permanent base/fork selected.** Define and own the event, memory, cursor, permission, and adapter contracts. Integrate through supported APIs and selectively reuse mature components. LiteLLM is a gateway candidate; OpenClaw is a serious runtime candidate; memory implementations should be evaluated as components. These are evaluation targets, not endorsed dependencies.

## Why this is the defensible current choice

The core product differentiator is portable, permission-aware knowledge and reliable handoff across independently operated tools. No candidate has yet been checked out or source-audited in this environment, so a firm fork recommendation would be unsupported. A fork before examining license, modules, tests, data model, and upstream cadence creates avoidable maintenance and legal risk. Composition preserves the option to replace runtimes and providers.

## Candidate decision matrix (provisional)

Scores are deliberately not invented. “Unknown” means no pinned source evidence, not poor quality.

| Candidate | Architecture fit | Functionality | License/security/tests | Maintenance/flexibility | Current decision |
|---|---|---|---|---|---|
| OpenClaw | Unknown; broad gateway/runtime could overlap | Unknown pending code | Unknown pending pinned audit | Unknown | Evaluate for integration; do not fork yet |
| Total Agent Memory | Potential memory subsystem fit | Unknown | Unknown | Unknown | Evaluate as subsystem/reference |
| Letta Code | Potential persistent-memory/agent model fit | Unknown | Unknown | Unknown | Serious alternative for memory concepts |
| LiteLLM | Provider gateway component candidate | Unknown pending audit | Unknown | Unknown | Prefer evaluate/integrate before own gateway |
| multiagents / Orchestra | Forum or coordinator concepts | Unknown | Unknown | Unknown | Compare narrowly; avoid adopting full runtime prematurely |

## Evaluation criteria

Score 1–5 with evidence for architecture compatibility, feature coverage, engineering effort, license compatibility, security boundaries, code quality/tests, modularity/scalability, upstream cadence, developer experience, and long-term flexibility. Record blocking unknowns separately. A permanent fork requires compelling unmet requirements, stable module seam, compatible licence, maintainable diff strategy, security review, and upstream merge plan.

## Review trigger

Revisit after core source audit and at least one composition spike: compare implementing a canonical event ingest + cursor adapter against candidate APIs. See ADR 0001. Alternatives: (1) OpenClaw-centered platform, (2) memory subsystem adoption plus independent sync service, (3) in-house minimal service. No final base selected.
