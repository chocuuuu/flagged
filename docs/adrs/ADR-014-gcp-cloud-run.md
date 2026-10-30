# ADR-014: Cloud Run for stateless application hosting

**Status:** Accepted

## Decision

study Cloud Run as the target stateless control/API runtime. Local development and Terraform validation are the default; deploying a Cloud Run service is optional and requires explicit cost approval.

## Context

it teaches stateless deployment and scale-to-zero behavior. A live service is not necessary to complete the project and may incur charges.

## Consequences

the application must be stateless and externalize durable state. The default learning path validates this design without applying infrastructure.
