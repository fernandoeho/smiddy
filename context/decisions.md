# Architecture Decision Records

This file is the authoritative log of significant architectural decisions. Each entry is an ADR (Architecture Decision Record).

The AI agent reads this file before Phase 02 (Design) and Phase 05 (Review) to avoid proposing changes that contradict standing decisions.

---

## How to Add an ADR

When you make a significant architectural decision during Phase 02, append a new entry below using this format:

```
## ADR-[N]: [Short title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Superseded by ADR-[N]

**Context:**
[Why this decision needed to be made. What forces, constraints, or options were in play.]

**Decision:**
[What was decided, stated directly.]

**Consequences:**
[What this enables and what it constrains. Include trade-offs honestly.]
```

When a decision is superseded, do not delete the old entry — update its status to `Superseded by ADR-[N]` and link to the new one.

---

## Decisions

_No decisions recorded yet. Add your first ADR when you make a significant architectural choice._

<!-- Example entry (delete this when you add your first real ADR):

## ADR-1: Use PostgreSQL as the primary data store

**Date:** 2025-01-15
**Status:** Accepted

**Context:**
We needed a relational database that supports ACID transactions and complex queries.
The team has strong existing PostgreSQL expertise. We considered MySQL and SQLite.

**Decision:**
Use PostgreSQL 16 as the primary data store for all persistent application state.

**Consequences:**
Enables complex joins, full-text search, and JSON column support.
Constrains deployment to environments where PostgreSQL is available or provisionable.
Local development requires a running Postgres instance (mitigated by Docker Compose).

-->
