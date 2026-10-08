# ADR-007: Persistence repository boundary

**Status:** Accepted

## Decision

isolate database operations behind a repository/service boundary.

## Context

the project deliberately compares PostgreSQL locally with Firestore in GCP.

## Consequences

domain logic can remain stable while persistence adapters vary; the abstraction must remain small and not become an accidental generic ORM.
