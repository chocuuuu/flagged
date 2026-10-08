# ADR-012: Scoped read-only client keys

**Status:** Accepted

## Decision

SDK clients receive environment-scoped read-only keys; admin credentials are separate.

## Context

browser applications are not trusted administrators.

## Consequences

the public client can request only SDK-safe configuration.
