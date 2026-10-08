# ADR-011: Deterministic hashing for percentage rollouts

**Status:** Accepted

## Decision

assign users to rollout buckets using a stable hash of flag key + subject key.

## Context

random per-request assignment would cause users to flip between variants.

## Consequences

stable assignment without server-side session state.
