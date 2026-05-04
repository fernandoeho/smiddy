# Setup: Architecture Discovery

**Purpose:** Scan an existing project and populate `.smiddy/context/architecture.md` with the actual system architecture.
**When to run:** Once, for existing projects, immediately after running `stack-discovery.md` and before starting Phase 02.
**Output:** A filled-in `.smiddy/context/architecture.md`.

> **New projects:** Do not run this prompt. The Architect agent in Phase 02 will create the architecture from scratch.

---

## Instructions

Your job is to discover the system's architecture by reading the source code — not by asking the user to describe it. Infer what you can; ask only what you cannot determine from the code itself.

### Step 1 — Map the top-level structure

Read the project root and identify the top-level folders. Determine whether the project is:

- A **monolith** — single deployable unit, all logic in one codebase
- A **modular monolith** — single deployment but code divided into explicit domain modules
- A **monorepo** — multiple packages or services in one repository
- A **microservices system** — multiple independently deployable services

Look for signals:
- `apps/`, `services/`, `packages/` folders → monorepo or microservices
- `src/` with domain-named subfolders → modular monolith
- Flat `src/` or single-layer structure → monolith

Record the architecture style and its rationale (as inferred from the code).

### Step 2 — Identify entry points

Find where the system starts:

| Signal | What it reveals |
|---|---|
| `main.ts`, `index.ts`, `app.ts`, `server.ts` | Application entry point |
| `cmd/`, `bin/`, `cli.py` | CLI entry points |
| `handler.ts`, `lambda.ts`, `functions/` | Serverless entry points |
| Route files (`routes/`, `pages/`, `app/` in Next.js) | HTTP surface area |
| Worker or queue consumer files | Background processing |

For each entry point, note what it exposes (HTTP, CLI, event, etc.) and to whom (public internet, internal services, scheduled jobs).

### Step 3 — Map components and responsibilities

Read the top-level source folders and identify distinct components. A component is a folder or module with a clear, bounded responsibility. For each component, describe:

- What it is responsible for
- What it depends on (other components, external services)
- Whether it has a public interface (exported functions, HTTP endpoints, events)

Do not list every file. Identify the boundaries, not the contents.

### Step 4 — Trace key data flows

Find the two or three most important user-facing or system-level flows. For each:

1. Start from the entry point (HTTP request, CLI command, event, scheduled job)
2. Follow the call chain through components
3. Identify where data is read from or written to

Use the format:
```
[Entry point] → [Component A] → [Component B] → [Data store or external service]
```

Focus on flows that cross component boundaries. Do not trace internal logic within a single component.

### Step 5 — Identify the persistence layer

Look for database models, schema files, and repository patterns:

| Signal | What it reveals |
|---|---|
| `prisma/schema.prisma`, `models/`, `entities/` | ORM models and data shape |
| `migrations/`, `db/migrate/` | Schema evolution history |
| `repositories/`, `daos/` | Data access abstraction |
| Direct query calls in service files | No abstraction layer |

For each data store used (identified in stack discovery), describe what data it holds and which components own access to it.

### Step 6 — Identify the auth model

Look for authentication and authorization patterns:

- Middleware files (`auth.middleware.ts`, `authenticate.py`, etc.)
- JWT or session handling code
- Permission guards or decorators (`@Guard`, `@Roles`, etc.)
- OAuth or third-party auth integration files

Describe: who authenticates, how sessions or tokens are issued and validated, and what the permission model looks like (RBAC, ABAC, ownership-based, etc.).

### Step 7 — Identify cross-cutting concerns

Scan for patterns used across the codebase:

| Concern | Where to look |
|---|---|
| Logging | Logger instantiation, log calls, logging middleware |
| Error handling | Global error handlers, error class hierarchies, try/catch patterns |
| Feature flags | Feature flag client usage, flag evaluation calls |
| Rate limiting | Rate limiter middleware or decorators |

Note the approach used for each — not the implementation details, but the strategy.

### Step 8 — Surface external dependencies

Look for API client instantiations, SDK imports, and HTTP client calls that reach outside the system. For each external dependency:

- What it is (third-party service name or internal service URL)
- Which component makes the call
- What operation is performed (read, write, notification, etc.)

Distinguish between external third-party services and internal services within the same organization.

### Step 9 — Fill in the architecture file

Write the discovered information into `.smiddy/context/architecture.md`. Follow these rules:

- Fill in only what you observed — do not guess or invent structure.
- Leave a section blank (with an italicised note) rather than writing anything you are not confident about.
- Update the **Last updated** date to today.
- Set **Status** to `Discovered — review recommended`.

### Step 10 — Surface what you could not determine

After writing the file, list any sections you left blank or marked uncertain, and explain what information would help fill them. Keep this list short — only items that will matter during Phase 02.

---

## Definition of Done

- [ ] `.smiddy/context/architecture.md` written with all discoverable sections filled in
- [ ] Architecture style identified with rationale
- [ ] At least two key data flows traced end-to-end
- [ ] Persistence and auth model described
- [ ] No invented structure — only observed facts
- [ ] Ambiguities noted inline in the file
- [ ] Remaining unknowns surfaced to the user as a short list
