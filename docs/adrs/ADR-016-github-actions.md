# ADR-016: GitHub Actions for CI/CD

**Status:** Accepted

## Decision

keep lint, test, and build commands runnable locally as the required path. GitHub Actions is an optional hosted CI/CD experiment and must remain disabled until its current usage quotas and cost implications are checked.

## Context

GitHub is the project's version-control platform.

## Consequences

local checks are reproducible without hosted minutes. Enabling hosted CI/CD requires a separate cost review; deployment workflows also require explicit approval before provisioning or deploying cloud resources.
