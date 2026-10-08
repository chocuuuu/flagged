# ADR-009: Polling before SSE before Pub/Sub

**Status:** Accepted

## Decision

implement configuration propagation progressively: REST bootstrap → polling → SSE → Pub/Sub.

## Context

each stage teaches a distinct distributed-systems concept.

## Consequences

the project takes longer but makes trade-offs measurable rather than abstract.
