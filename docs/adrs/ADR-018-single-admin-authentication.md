# ADR-018: Single-operator admin authentication

**Status:** Accepted

## Context

Flagged is a personal learning project with one administrative operator. It needs to protect configuration mutations without introducing user registration, role management, an external identity provider, or persistent session infrastructure before those concepts are needed.

The admin dashboard is a browser application. Browser-held bearer tokens are exposed to JavaScript and are easier to leak through XSS than an `HttpOnly` cookie. Long-lived JWTs also complicate logout and revocation. A server-side session database would add state and another persistence concern to a service intended to be stateless.

## Decision

- Support one configured admin identity; do not implement multi-user accounts, invitations, or roles in the initial project.
- Verify the admin password with `pwdlib` using Argon2id. This is a deliberately selected dependency because password hashing should use a maintained implementation, not custom cryptography or a general-purpose hash. Store only the verifier in local environment configuration; never commit or log the password or verifier.
- Use Starlette's signed session-cookie middleware with a one-hour maximum age and only minimum non-sensitive identity/expiry claims. Its signing key comes from local environment configuration, not source control. The cookie is tamper-evident, not encrypted.
- Configure the cookie as `HttpOnly` and `SameSite=Lax`; set `Secure` whenever served over HTTPS. Prefer serving the dashboard and admin API from the same origin.
- Protect every state-changing browser request with CSRF defenses: validate the request origin and require a CSRF token. Keep the dashboard and admin API same-origin where practical.
- Do not persist server-side sessions. Expiry bounds a session; rotating the signing key invalidates all sessions.
- Keep environment-scoped SDK client keys separate and read-only. They never authenticate as the administrator.
- Use local configuration for the default $0 path. Any live-cloud secret delivery requires a separate cost/security review and explicit opt-in.

## Alternatives considered

### JWT bearer token in browser storage

Rejected because JavaScript can read browser storage, increasing exposure to XSS, and revocation/refresh adds complexity.

### Server-side sessions

Rejected for the initial single-operator scope because durable session storage adds infrastructure and operational work without a current multi-user need.

### Hosted identity provider

Rejected as the default because it adds an external service, account configuration, and possible cost while obscuring the authentication fundamentals this project intends to learn.

## Consequences

The model is deliberately small and suitable only for a personal, single-admin system. Signed cookies are tamper-evident, not encrypted; their contents must remain non-sensitive. Key rotation logs out every session. CSRF defenses and password-hashing configuration still require tests. If the project gains multiple users or public production exposure, revisit this ADR before expanding authentication.
