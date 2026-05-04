# Setup: Stack Discovery

**Purpose:** Scan an existing project and populate `.smiddy/context/stack.md` with the actual tech stack.
**When to run:** Once, immediately after installing Smiddy into a project that already has code.
**Output:** A filled-in `.smiddy/context/stack.md`.

---

## Instructions

Your job is to discover the project's tech stack by reading its files — not by asking the user to describe it. Infer what you can; ask only what you cannot determine from the project itself.

### Step 1 — Scan for language and runtime indicators

Look for files that reveal the primary languages and their versions:

| File | What it reveals |
|---|---|
| `package.json`, `.nvmrc`, `.node-version` | Node.js version, JS/TS usage |
| `tsconfig.json` | TypeScript and target |
| `pyproject.toml`, `setup.py`, `requirements*.txt`, `.python-version` | Python version and packaging tool |
| `go.mod` | Go version and module name |
| `Gemfile`, `.ruby-version` | Ruby version |
| `pom.xml`, `build.gradle` | Java/Kotlin version and build tool |
| `Cargo.toml` | Rust version |
| `*.csproj`, `global.json` | .NET version |
| `composer.json` | PHP version |

Record each language found, its version (if determinable), and its primary use.

### Step 2 — Scan for frameworks and libraries

Read `package.json` (dependencies + devDependencies), `requirements*.txt`, `pyproject.toml`, `Gemfile`, `go.mod`, `pom.xml`, `build.gradle`, or equivalent. Identify:

- Web frameworks (React, Next.js, Vue, Django, Rails, FastAPI, etc.)
- Testing libraries (Jest, Vitest, pytest, RSpec, etc.)
- ORM / database clients (Prisma, SQLAlchemy, ActiveRecord, etc.)
- Any other significant libraries worth noting

Do not list every dependency — list only those that meaningfully constrain how the system is built or tested.

### Step 3 — Scan for data stores

Look for configuration files, environment variable references, and connection string patterns:

- Database URLs in `.env`, `.env.example`, `docker-compose.yml`, config files
- ORM configuration files (e.g., `database.yml`, `alembic.ini`, `prisma/schema.prisma`)
- Cache references (Redis, Memcached)
- Queue or stream references (RabbitMQ, Kafka, SQS, Celery)
- Search engine references (Elasticsearch, Algolia, Typesense)
- Object storage references (S3, GCS, Azure Blob)

If a `.env.example` or similar template exists, prefer it over `.env` (which may not be committed).

### Step 4 — Scan for infrastructure and CI/CD

Look at:

- `Dockerfile`, `docker-compose.yml` — container runtime and service topology
- `.github/workflows/*.yml`, `.gitlab-ci.yml`, `Jenkinsfile`, `circle.yml` — CI/CD tooling
- `terraform/`, `*.tf`, `pulumi/`, `cdk/` — infrastructure as code and cloud provider
- `k8s/`, `helm/`, `*.yaml` with Kubernetes resource kinds — container orchestration
- Cloud SDK references in CI files — hosting provider (AWS, GCP, Azure, Vercel, Fly, etc.)

### Step 5 — Scan for developer tooling

Look for config files that reveal the toolchain:

| File | Tool |
|---|---|
| `.eslintrc*`, `eslint.config.*` | ESLint |
| `.prettierrc*` | Prettier |
| `ruff.toml`, `.flake8`, `pyproject.toml [tool.ruff]` | Python linter |
| `jest.config.*`, `vitest.config.*` | Test runner |
| `vite.config.*`, `webpack.config.*`, `rollup.config.*` | Build tool |
| `package.json` (`packageManager` field) | Package manager (npm/yarn/pnpm/bun) |
| `Makefile` | Common task runner targets |

### Step 6 — Scan for external services

Look in `.env.example`, README, and CI configs for references to third-party services:
- Authentication providers (Auth0, Clerk, Cognito, etc.)
- Payment processors (Stripe, etc.)
- Email services (SendGrid, Resend, etc.)
- Monitoring and observability (Datadog, Sentry, OpenTelemetry, etc.)
- Feature flag services, analytics platforms, etc.

For each, note its purpose and the auth method used (API key, OAuth, service account, etc.) if determinable.

### Step 7 — Note conventions for standards discovery

Do not write conventions to `stack.md`. Coding conventions (naming, file structure, error handling, response shapes, etc.) belong in `.smiddy/governance/standards/` where they are indexed and selectively loaded per phase.

While scanning, note any strong conventions you observe — branch naming patterns, commit format, file structure style, error handling approach. Surface these to the user at the end as a short list so they know which areas to target first when running `standards-discovery.md`.

### Step 8 — Fill in the stack file

Write the discovered information into `.smiddy/context/stack.md`. Follow these rules:

- Fill in only what you observed — do not guess or invent versions.
- Leave a cell blank rather than writing "unknown" or "N/A".
- Add a comment in italics below any section where important details were ambiguous.
- Do not remove table rows — leave them blank if the concern does not apply.

### Step 9 — Surface what you could not determine and suggest standards areas

After writing the file:

1. List any fields you left blank that are likely relevant to the project, and explain what information would be needed to fill them. Keep this list short — only items that will matter during pipeline phases.

2. List the conventions you noted in Step 7 as suggested focus areas for `standards-discovery.md`. For example: "Observed consistent error handling patterns in `src/` — good candidate for a standard."

---

## Definition of Done

- [ ] `.smiddy/context/stack.md` written with all discoverable fields filled in
- [ ] No invented or guessed values — only observed facts
- [ ] Ambiguities noted inline in the file
- [ ] Remaining unknowns surfaced to the user as a short list
