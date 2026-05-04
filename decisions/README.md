# Architecture Decision Records

ADRs live as individual files in `.smiddy/decisions/`. Use `.smiddy/decisions/index.yml` to find ADRs by area without loading every decision.

The AI agent reads `index.yml` before Phase 02 (Design) and Phase 04 (Review) to identify which ADR files are relevant to the current work.

---

## How to Add an ADR

1. Determine the next ADR number from `index.yml`.
2. Create `.smiddy/decisions/ADR-NNN-short-title.md` using the format below.
3. Add an entry to `.smiddy/decisions/index.yml` with appropriate area tags.

When a decision is superseded, do not delete the old file — update its status to `Superseded by ADR-NNN` in both the file and the index.

---

## ADR File Format

```markdown
# ADR-NNN: [Short title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Superseded by ADR-NNN

## Context

[Why this decision needed to be made. What forces, constraints, or options were in play.]

## Decision

[What was decided, stated directly.]

## Consequences

[What this enables and what it constrains. Include trade-offs honestly.]
```

---

## Example

See `ADR-001-example.md` for a worked example of the format.
