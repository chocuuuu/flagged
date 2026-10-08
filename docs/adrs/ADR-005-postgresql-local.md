# ADR-005: PostgreSQL as local source of truth

**Status:** Accepted

## Decision

PostgreSQL is the initial local database.

## Context

relational constraints, transactions, indexes, and migrations are valuable backend/cloud skills.

## Consequences

the local model is richer than a key-value store and later requires an explicit cloud persistence mapping.
