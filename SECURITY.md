# SECURITY.md

# Flagged — Security Model

## 1. Security objective

Protect:

- admin operations
- flag configuration integrity
- client credentials
- audit records
- cloud infrastructure

while keeping the demo simple enough to understand.

---

# 2. Threat model

Primary threats:

| Threat | Example |
|---|---|
| Credential theft | leaked admin token |
| Privilege escalation | SDK key calling admin API |
| Configuration tampering | unauthorized flag change |
| Client key abuse | public endpoint scraping |
| Secret leakage | tokens committed to Git |
| Replay/stale config | old update overwrites new state |
| Data exposure | admin-only configuration exposed |
| Denial of service | excessive flag/config requests |
| Misconfigured IAM | over-privileged Cloud Run service |
| Logging leakage | secret in logs |

---

# 3. Trust zones

```text
                 Untrusted
                    │
                    ▼
              Demo Browser
                    │
             scoped client key
                    │
                    ▼
              SDK endpoint
                    │
        ┌───────────┴───────────┐
        │                       │
   Control plane           Data plane
        │                       │
   admin auth              client auth
        │                       │
        ▼                       ▼
      DB/config            published config
```

---

# 4. Authentication

## Admin

For the learning MVP:

- username/email + password
- session/JWT
- secure password hashing

Do not invent cryptographic algorithms. Use a reputable password-hashing library.

## Client SDK

Use an environment-scoped client key.

The client key can read SDK-safe configuration but must not:

- create flags
- modify flags
- read admin audit data
- read credentials

---

# 5. Authorization

Minimum roles:

```text
ADMIN
VIEWER
```

Admin:

- create/update/delete configuration
- manage client keys
- view audit history

Viewer:

- read configuration through dashboard
- cannot mutate flags

SDK:

- evaluation/read-only configuration only

---

# 6. Key handling

Store only a hash of client secrets where possible.

Display only:

```text
ff_client_abc123••••••
```

When a key is created:

```text
generate
   ↓
show once
   ↓
hash
   ↓
store hash
```

Revocation:

```text
active → revoked
```

---

# 7. Secret management

Local:

```text
.env
.env.example
```

`.env` must be ignored by Git.

Cloud:

- prefer platform-injected secrets/variables;
- Secret Manager is optional if needed;
- never embed admin credentials in frontend assets.

Because this project prioritizes zero cost, any paid-secret-management feature must be evaluated before adoption.

---

# 8. SDK/browser security boundary

The browser SDK is not a trusted administrator.

A public client key should expose only the minimum configuration necessary for flag evaluation.

Never put:

```text
ADMIN_SECRET
DATABASE_URL
JWT_SIGNING_SECRET
SERVICE_ACCOUNT_KEY
```

into the browser.

---

# 9. API protections

Admin API:

- authentication required
- authorization required
- input validation
- rate limiting
- secure headers
- controlled CORS
- structured error messages

SDK API:

- scoped client authentication
- caching
- ETags/version checks
- rate limits appropriate to the learning environment

---

# 10. Configuration integrity

Every distributed configuration has a version.

SDK rule:

```text
accept incoming version
ONLY IF
incoming.version > local.version
```

This protects against stale updates.

---

# 11. Network security

Use HTTPS in deployed environments.

Never disable certificate validation to "make it work."

For local development, HTTP is acceptable within the developer machine.

---

# 12. Audit logs

Every mutation should generate an audit event containing:

- actor
- action
- resource
- timestamp
- old value
- new value

Do not log secrets.

---

# 13. Cloud IAM

Principle:

> grant the minimum permission needed.

The Cloud Run service should not automatically have broad project-level permissions.

Example desired separation:

```text
Cloud Run runtime
  ├── Firestore access
  └── Pub/Sub publish/consume as required
```

It should not have:

```text
Owner
Editor
Broad project admin
```

permissions.

IAM API usage itself is free according to Google's current pricing documentation.

---

# 14. Abuse scenarios

Test:

```text
invalid client key
revoked client key
expired admin session
oversized payload
too many requests
malformed targeting rule
attempt to mutate SDK endpoint
```

---

# 15. Security testing

Tools/practices:

- pytest security cases
- dependency audit
- secret scanning
- GitHub secret scanning where available
- Gitleaks
- OWASP API Security guidance
- manual abuse tests

---

# 16. Security definition of done

No release is complete if:

- secrets are committed;
- admin API can be called without authorization;
- SDK key can mutate configuration;
- revoked keys still work;
- stale configuration can overwrite newer configuration;
- sensitive values are visible in logs.
