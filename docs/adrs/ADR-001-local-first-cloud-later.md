# ADR-001: Local-first development and cloud-later migration

**Status:** Accepted

## Decision

develop and validate the entire core system locally before provisioning GCP resources.

## Context

the project is intended as a learning exercise and must minimize cost.

## Consequences

more work is required to make local infrastructure reproducible, but debugging is cheaper and architectural understanding is stronger.
