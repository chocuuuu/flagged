# ADR-013: Do not require managed Redis

**Status:** Accepted

## Decision

Redis is local-only by default.

## Context

managed Memorystore is provisioned and billable even when idle.

## Consequences

shared-cache learning happens locally; the cloud architecture avoids a predictable always-on cost.
