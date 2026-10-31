# Reset and recreate the local database

**Status:** Draft; validate exact service and migration names when local
infrastructure is implemented.

> **Destructive:** removing the local database volume permanently deletes its data.
> Confirm the Compose project and volume are local before proceeding.

1. Stop local services with `docker compose down`.
2. If a clean database is intentionally required, remove only the named local
   PostgreSQL volume using the project's documented Compose volume name. Do not use
   an unqualified prune command.
3. Recreate services with `docker compose up -d`.
4. Apply migrations from an empty database.
5. Verify health, schema version, and a representative API read.
6. Record the command and result; restore only from an explicitly created local
   backup if data was needed.

Never point this runbook at a cloud or shared database.
