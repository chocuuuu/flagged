# Local setup runbook

**Status:** Draft; verify commands when the Compose and application files are
implemented in Sprint 1.

1. Install the pinned Python, Node.js, uv, pnpm, and Docker/Compose versions from
   `DEPENDENCIES.md`.
2. Clone the repository and copy `.env.example` to `.env` only after that example
   exists. Never commit `.env`; keep admin credentials out of the browser and demo.
3. Start local dependencies with `docker compose up -d`.
4. Verify PostgreSQL health with the documented Compose health check.
5. Apply migrations using the repository's documented local command.
6. Start the API, dashboard, and demo store using their local run commands.
7. Verify the API health endpoint and load the demo in a browser.

Do not run Terraform apply or enable hosted cloud services for local setup.
