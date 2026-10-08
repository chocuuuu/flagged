# ADR-006: Firestore as default GCP persistence path

**Status:** Accepted

## Decision

use Firestore for the low-cost GCP deployment path.

## Context

the project prioritizes minimal spend and wants managed/serverless cloud practice.

## Consequences

the data model must be intentionally adapted; Firestore is not treated as a drop-in PostgreSQL substitute.
