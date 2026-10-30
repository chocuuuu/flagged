# ADR-009: Polling before SSE before Pub/Sub

**Status:** Accepted

## Decision

implement configuration propagation progressively: REST bootstrap → polling → SSE → Pub/Sub. Run each stage locally or with an emulator/adapter by default; live Pub/Sub use is optional and requires cost approval.

## Context

each stage teaches a distinct distributed-systems concept. Local implementations provide the default $0 path.

## Consequences

the project takes longer but makes trade-offs measurable rather than abstract.
