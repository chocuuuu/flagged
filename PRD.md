# PRD.md

# Flagged
## Distributed Feature Flag & Configuration Platform

**Status:** Approved planning baseline  
**Duration:** 12 weeks / 60 working sessions  
**Primary goal:** Learn cloud and system design by building, testing, breaking, and improving a real distributed platform.

---

# 1. Problem statement

Software teams often want to deploy code without immediately releasing a new behavior to every user.

Traditional deployment-only release flow couples:

```text
code deployment
      +
user exposure
```

This creates operational pressure when:

- a feature is incomplete;
- a feature needs a gradual rollout;
- only internal/beta users should receive it;
- production behavior must be disabled quickly;
- a team wants to separate deployment from release.

A feature-flag platform separates these concerns.

The central platform stores and manages configuration, while consuming applications evaluate flags locally from configuration distributed by the platform.

---

# 2. Product vision

Build a small-scale alternative to the core capabilities of a commercial feature-management platform.

The product should let a developer:

1. Create a project.
2. Create environments.
3. Create feature flags.
4. Enable/disable a flag.
5. Configure a percentage rollout.
6. Define simple targeting rules.
7. Issue a client SDK key for an environment.
8. Allow a demo application to retrieve configuration.
9. Evaluate flags locally in the SDK.
10. Propagate updates without requiring application redeployment.
11. Observe configuration propagation and evaluation behavior.

---

# 3. Real-world analogy

A production application contains the new behavior, but a runtime decision determines whether users enter that code path.

Example:

```text
new_checkout = OFF

Application:
if flag("new_checkout"):
    new_checkout()
else:
    old_checkout()
```

Turning the flag off does not necessarily roll back the deployment. It changes runtime behavior.

Commercial products such as LaunchDarkly and standards/projects such as OpenFeature provide related concepts. This project implements a learning-focused subset.

---

# 4. Target user

Primary user:

**Developer / small engineering team**

They need to:

- safely introduce a feature;
- test new behavior with a limited population;
- disable behavior quickly;
- manage different environments;
- integrate an application through an SDK.

Secondary user:

**Platform administrator**

They manage projects, environments, flags, rules, and audit information.

---

# 5. Demo application

Only one demo application is required:

## Flagged Demo Store

An intentionally small Astro + React storefront.

Pages/features:

- Home
- Product list
- Product detail
- Cart
- Checkout

The storefront exists to demonstrate the platform. It is not intended to become a complete e-commerce product.

Demo flags:

```text
new_checkout
new_product_card
holiday_banner
```

---

# 6. Functional requirements

## FR-01 Projects

Users can create and view projects.

## FR-02 Environments

Each project supports:

- development
- staging
- production

## FR-03 Feature flags

A flag has:

- stable key
- display name
- description
- type
- enabled state
- environment
- version
- timestamps

## FR-04 Boolean evaluation

The SDK must support:

```text
isEnabled(flagKey, context)
```

## FR-05 Percentage rollout

Support deterministic user bucketing.

## FR-06 Targeting

Initial targeting should support a deliberately small rule set:

```text
attribute equals value
attribute contains value
```

Stretch:

- AND/OR groups
- multiple rules
- variants

## FR-07 Configuration bootstrap

SDK can fetch an environment configuration.

## FR-08 Local evaluation

After configuration is loaded, normal flag evaluations should not require a network request.

## FR-09 Polling

SDK can periodically refresh configuration.

## FR-10 Streaming

SDK can optionally maintain an SSE connection for update events.

## FR-11 Versioning

Every configuration update has a monotonically increasing version.

The SDK must ignore an older configuration received after a newer one.

## FR-12 Audit log

Record:

- who changed a flag
- what changed
- previous value
- new value
- timestamp

## FR-13 Safe fallback

When the platform cannot be reached, the SDK uses:

1. last known good configuration;
2. otherwise caller-specified default.

## FR-14 API keys

SDK/client keys must be scoped to a project/environment and must not have administrative privileges.

---

# 7. Non-functional requirements

## NFR-01 Low evaluation latency

Local evaluation should be orders of magnitude cheaper/faster than a network round trip.

Exact target will be benchmarked rather than assumed.

## NFR-02 Propagation target

Target configuration propagation:

**< 5 seconds under normal demo conditions**

This is an engineering target, not a correctness guarantee.

## NFR-03 Availability

A temporary flag service outage should not automatically break the demo application.

## NFR-04 Idempotency

Repeated update events must not corrupt SDK state.

## NFR-05 Observability

The system should expose enough telemetry to answer:

- How long does evaluation take?
- How quickly do updates propagate?
- How many updates fail?
- How often is stale configuration used?

## NFR-06 Reproducibility

A new developer should be able to run the core system locally using documented commands.

## NFR-07 Cost

Core development target: **$0**.

Cloud deployment target: **near $0 and designed around free-tier-compatible usage**.

---

# 8. Scope by phase

## MVP

- Python/FastAPI API
- PostgreSQL
- admin authentication
- project/environment/flag CRUD
- boolean evaluation
- TypeScript SDK
- in-memory configuration
- demo store integration
- tests
- Docker Compose

## Phase 2

- percentage rollout
- targeting
- audit logs
- versioning
- polling
- Redis cache experiment

## Phase 3

- SSE
- reconnection
- stale-cache strategy
- observability
- load testing
- failure injection

## Phase 4

- GCP deployment
- Firestore adapter
- Pub/Sub propagation
- IAM
- Artifact Registry
- Terraform
- GitHub Actions

---

# 9. Explicit non-goals

Do not build initially:

- enterprise SSO
- SAML
- billing
- multi-region deployment
- A/B experimentation analytics
- complex rule DSL
- mobile SDKs
- native Java SDK
- Kubernetes
- service mesh
- multi-cloud deployment
- a full production e-commerce backend

These may be discussed, not implemented.

---

# 10. Success criteria

The project succeeds when:

1. A developer can create a flag from the dashboard.
2. The demo application consumes it through the SDK.
3. A flag can be turned on/off without rebuilding the demo app.
4. A 10% rollout deterministically selects users.
5. SDK evaluations normally execute locally.
6. The SDK can refresh configuration via polling.
7. The SDK can receive updates via SSE.
8. Update versions prevent stale writes.
9. The system survives temporary control-plane failures using cached configuration.
10. Tests cover core behavior and failure cases.
11. The system is containerized.
12. The infrastructure can be recreated with Terraform.
13. A GCP deployment exists within the project's cost guardrails.
14. A final report explains architecture decisions and measured behavior.

