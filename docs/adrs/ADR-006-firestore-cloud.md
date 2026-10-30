# ADR-006: Firestore as an optional cloud persistence experiment

**Status:** Proposed

## Decision

study Firestore through its local emulator by default. A live Firestore adapter is an optional GCP experiment that is not required for project completion.

## Context

the project targets $0 in cloud-service charges by default while still learning document modeling and the managed-service boundary locally.

## Consequences

the data model must be intentionally adapted; Firestore is not treated as a drop-in PostgreSQL substitute. Live service use requires explicit approval after current pricing, billing, and cleanup review.
