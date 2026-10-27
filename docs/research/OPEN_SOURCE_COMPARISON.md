# Open-source project comparison

**Evidence status:** this is an initial candidate map, not a completed source-level comparison. Direct source clones were blocked by the local network proxy. Candidate-specific feature statements below are hypotheses to verify, not implementation findings. The cited repositories are mutable default-branch links until pinned revisions are available.

| Candidate | Apparent fit to investigate | Main gap/questions for AI_Uni | Status |
|---|---|---|---|
| OpenClaw | Broad gateway and agent runtime; session concepts | Can its tenancy, external harness boundary and durable event/cursor model serve independent CLIs? | Source audit pending |
| Total Agent Memory | Cross-client memory/MCP focus | Verify storage, evidence/version semantics, incremental sync, license and claims under tests | Source audit pending |
| multiagents | Agent messaging/orchestration | Verify actual broker durability, licensing, ACLs and adapter coverage | Source audit pending |
| Orchestra | Coding-agent terminal coordination | Check reconnection, worktree isolation, ownership and security | Source audit pending |
| Letta Code | Persistent memory blocks and agent identity | Check local/hosted dependencies, memory export, user-owned project scope | Source audit pending |
| OpenHands + SDK | Software-agent runtime and SDK boundaries | Evaluate ACP/server/client seams and isolated execution; not shared memory by itself | Source audit pending |
| Hermes Agent | Agent runtime | Evaluate external CLI interoperability, memory and permissions | Source audit pending |
| Moyai | Gateway/agent infrastructure candidate | Confirm repository identity, maturity, current functionality and fit | Source audit pending |
| OpenCode | Coding-agent CLI/runtime | Study extensibility and supported integration surfaces | Source audit pending |
| LibreChat | Multi-provider chat application | Potential UI/provider reuse; project/session memory contract likely separate | Source audit pending |
| Open WebUI | Local/provider UI platform | Potential UI/inference integrations; evaluate permissions and API contracts | Source audit pending |
| Mem0 / OpenMemory | Memory subsystem candidates | Evaluate provenance, scope isolation, temporal conflict and deletion behavior | Source audit pending |
| Graphiti | Temporal graph retrieval | Potential retrieval component; assess operational complexity and evidence semantics | Source audit pending |
| LiteLLM | Provider gateway | Candidate to compose for routing, providers and usage; verify current features/licence | Source audit pending |
| Codex | Target client/runtime integration | Official app-server/API surfaces and versioned event semantics to verify | Source audit pending |

## Provisional conclusion

No full application is yet proven to satisfy the user-owned, cross-runtime event and memory contract. Prefer composition while defining the contract. Evaluate OpenClaw as the broad runtime candidate, LiteLLM for gateway functions, and memory-specific projects as subsystem references. Do not select or fork based on repository descriptions alone. Detailed scoring is deferred until pinned source and tests are inspected (`FORK_DECISION.md`).
