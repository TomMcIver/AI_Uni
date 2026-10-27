# Model gateway

**Status: future, not implemented.** Evaluate LiteLLM before implementing provider routing, credentials, model aliases, streaming, usage/cost, rate limits and capability metadata. Keep memory/event contracts provider-agnostic. Do not duplicate mature gateway features without documented gaps.

Capability registry should record provider/model identity, modalities, context/output limits, tools/structured output, streaming, residency/retention constraints, measured quality/latency/cost provenance, and update time. Treat capability claims as versioned/unverified until checked. Credentials belong in a secrets boundary, never event or memory records. Local Ollama/vLLM integrations are optional adapters.

Gateway availability must not be required to sync project memory. Future UI may invoke providers through a gateway or direct adapters, but provider replacement must not migrate core memory semantics.
