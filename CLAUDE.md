# CLAUDE.md

> Project: **Flagged — Distributed Feature Flag & Configuration Platform**
> Canonical agent instructions live in `AGENTS.md`. This file contains Claude Code-specific workflow guidance.

## 1. Project mission

The goal is not to generate a feature-flag platform as quickly as possible. The goal is to **learn cloud engineering and distributed-system design through deliberate implementation, testing, debugging, and iteration**.

AI is an engineering assistant, not the author of the learning process.

## 2. Non-negotiable AI behavior

Before modifying code for a non-trivial task, the agent should:

1. Explain the architectural purpose of the change.
2. Identify assumptions and dependencies.
3. State what files/components it expects to touch.
4. State what tests should prove the change.
5. Implement the smallest useful increment.
6. Run or specify the relevant tests.
7. Explain failures instead of hiding them.
8. Never remove a test simply because it fails.
9. Never introduce a dependency without explaining why it is needed.
10. Never create secrets, credentials, real API keys, or personal data.
11. Never silently change architecture, storage semantics, or public SDK behavior.

## 3. Learning-first rule

When a task introduces a new concept, the agent must first provide a short "Concept checkpoint":

- What problem does this concept solve?
- Why is it needed here?
- What simpler approach did we have before?
- What trade-off are we introducing?
- How can the user verify it experimentally?

Examples:

- Redis: explain cache-aside and invalidation before implementing it.
- SSE: explain long-lived HTTP connections before adding the stream.
- Pub/Sub: explain at-least-once delivery and idempotency before wiring events.
- Firestore: explain document semantics and free-tier constraints before migrating.
- Cloud Run: explain stateless deployment and scale-to-zero behavior before deployment.

## 4. Preferred AI loop

Use:

```text
Understand → Design → Implement → Test → Debug → Measure → Document
```

Do not use:

```text
Prompt → Generate entire application → Hope it works
```

## 5. Debugging protocol

When a test or runtime behavior fails:

1. Reproduce it.
2. Isolate the boundary where behavior diverges.
3. Form one or more hypotheses.
4. Add the smallest useful diagnostic.
5. Fix the root cause.
6. Add/regress a test.
7. Document the lesson when architectural.

## 6. Code-generation limits

Avoid:

- giant one-shot implementations
- unrelated refactors
- "cleanup" during feature work
- framework replacement without an ADR
- speculative abstractions
- premature microservices

Prefer:

- small commits
- narrow pull requests
- explicit interfaces
- typed request/response models
- tests next to the behavior they protect
- boring infrastructure that is easy to destroy and recreate

## 7. Dependency policy

Every new dependency needs:

- purpose
- alternatives considered
- maintenance/complexity impact
- cost impact, if any
- whether standard-library functionality could reasonably solve the need

## 8. Security policy

Never:

- commit `.env`
- hard-code API keys
- place admin credentials in the client SDK
- expose admin API credentials to the demo application
- log access tokens or secrets
- disable TLS verification in normal code
- broaden IAM permissions "temporarily" without documenting and reverting them

## 9. Git workflow

Use:

```text
main
└── feature/<short-name>
```

For meaningful changes:

- issue-linked branch
- focused commit
- tests included
- PR description
- review/checks
- merge
- delete branch

Commit style:

```text
feat(scope): ...
fix(scope): ...
test(scope): ...
refactor(scope): ...
docs(scope): ...
infra(scope): ...
chore(scope): ...
```

## 10. Agent autonomy

The agent may autonomously:

- read the repository
- propose implementation steps
- create tests
- run local tools
- make small code changes within the approved task
- update documentation

The agent should pause and ask for user direction only when:

- a requirement is genuinely ambiguous and materially changes architecture;
- an external paid service may be created;
- a destructive cloud action could create cost/data loss;
- credentials or permissions are required that the user has not explicitly provided.

For ordinary implementation ambiguity, choose the smallest reversible option and document the decision.

## 11. Cloud cost gate

Before introducing any managed GCP resource that can incur charges:

```text
1. Identify the service.
2. Check its current pricing/free tier.
3. Estimate this project's expected usage.
4. Tell the user whether the step is optional or required.
5. Prefer a local/emulated alternative when the learning objective is unchanged.
6. Add deletion/cleanup commands.
```

Never create an always-on paid resource merely because a reference architecture commonly uses it.

## 12. Definition of done for AI-assisted work

A task is not done merely because code was written.

It is done when:

- behavior matches acceptance criteria;
- relevant tests pass;
- failure behavior is understood;
- documentation is updated when necessary;
- no secrets are introduced;
- the user can explain the key design decision;
- the change has a focused commit.

