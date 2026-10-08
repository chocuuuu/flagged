# ADR-008: Evaluate feature flags in the SDK

**Status:** Accepted

## Decision

normal evaluations occur locally from an in-memory configuration snapshot.

## Context

feature checks are on the application's hot path.

## Consequences

low latency and resilience, but configuration synchronization becomes a first-class problem.
