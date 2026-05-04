# ADR-001: Use PostgreSQL as the primary data store

**Date:** 2025-01-15
**Status:** Accepted

## Context

We needed a relational database that supports ACID transactions and complex queries.
The team has strong existing PostgreSQL expertise. We considered MySQL and SQLite.

## Decision

Use PostgreSQL 16 as the primary data store for all persistent application state.

## Consequences

Enables complex joins, full-text search, and JSON column support.
Constrains deployment to environments where PostgreSQL is available or provisionable.
Local development requires a running Postgres instance (mitigated by Docker Compose).
