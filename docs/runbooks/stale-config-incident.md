# Stale configuration incident

1. Record the environment, client snapshot revision, latest server revision, request
   IDs, and timestamps. Do not collect client keys or personal evaluation context.
2. Check local API/database health and whether the client is retaining its
   last-known-good snapshot as required.
3. For SSE, check stream connectivity and whether `config.updated` carried the
   expected revision. The SDK must fetch the complete snapshot after a hint or
   reconnect.
4. Trigger a safe bootstrap/conditional refresh and compare the resulting revision.
   Never install an equal or older revision.
5. If refresh fails, preserve the current valid snapshot and record the failure; do
   not clear cached configuration to make the symptom disappear.
6. Verify recovery with a repeatable test and record the stale interval and cause.
