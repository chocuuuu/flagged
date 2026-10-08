# ADR-002: Modular monolith before microservices

**Status:** Accepted

## Decision

use a modular FastAPI service rather than multiple independently deployed microservices.

## Context

the project already has distributed concerns in SDK propagation and eventing.

## Consequences

fewer operational boundaries and easier debugging; later service splitting is an experiment, not a starting requirement.
