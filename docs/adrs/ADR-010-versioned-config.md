# ADR-010: Monotonic configuration versions

**Status:** Accepted

## Decision

every configuration snapshot has a monotonic version; clients accept only newer versions.

## Context

distributed update events can be duplicated or reordered.

## Consequences

simple idempotency/staleness protection with a small state model.
