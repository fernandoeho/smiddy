# Gate: Design → Build

**When to check:** At the start of Phase 03, before writing any code.
**How to check:** Open the active spec and verify each item below.
**On failure:** Stop. List every failing item. Ask the user to complete Phase 02 before Phase 03 proceeds.

---

## 1. Artifact

- [ ] Spec file exists at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md`
- [ ] Spec status is `In Review` (not `Draft` or unfilled)

---

## 2. Completeness

Each section below must be filled in — not a placeholder, not the template's italic hint text.

- [ ] **Proposed Design** — at least one paragraph describing the approach
- [ ] **Affected Components** — at least one row in the table with a named component and change type
- [ ] **Interface Contracts** — present and describes each new or changed public interface

---

## 3. Quality

This gate's quality bar is *implementability*: a Developer must be able to write code from the spec without making design decisions themselves.

- [ ] Every interface contract is explicit — it includes name, inputs, outputs, and error cases; prose descriptions alone do not pass
- [ ] Every component in "Affected Components" is named specifically enough to locate in the codebase (no entries like "some service" or "the backend")
- [ ] If persistent data is created or modified: "Data Model Changes" is filled in and includes a migration strategy
- [ ] If an architecturally significant decision was made: a corresponding ADR file exists in `.smiddy/governance/decisions/` and `index.yml` is updated
- [ ] No section contains `TBD`, `TODO`, or unresolved placeholder text

---

## 4. Blockers

- [ ] Open Questions table has no unresolved entries marked as blockers
- [ ] No interface contract is under-specified to the point where implementing it would require guessing

---

## Gate Result

**Pass** — all items checked → proceed to Phase 03.

**Fail** — one or more items unchecked → do not start implementation. Report the failing items to the user with a brief explanation of what is missing or too vague, then stop.
