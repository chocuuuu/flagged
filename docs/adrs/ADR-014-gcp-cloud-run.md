# ADR-014: Cloud Run for stateless application hosting

**Status:** Accepted

## Decision

use Cloud Run for the control/API service.

## Context

it fits the project's existing GCP knowledge and supports scale-to-zero request-based deployment.

## Consequences

the application must be stateless and externalize durable state.
