# Revoke a client key

1. Authenticate to the admin dashboard using the configured admin session.
2. Select the affected project and environment; confirm the key metadata and
   `keyPrefix` without exposing or logging the full secret.
3. Revoke the key using the admin client-key action (contract:
   `DELETE /v1/admin/projects/{projectKey}/environments/{environmentKey}/client-keys/{clientKeyId}`).
4. Confirm the key metadata reports `revoked`; never attempt to retrieve the original
   secret because it is shown only once.
5. Verify a fresh SDK config request with that key is rejected. An already-open SSE
   stream may persist until it closes; verify subsequent snapshot requests fail.
6. Rotate the key in the consuming app through its normal secret/configuration
   process. Do not put an admin credential in the browser or demo app.
