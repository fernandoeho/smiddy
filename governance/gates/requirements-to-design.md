# Gate: Requirements → Design

**When to check:** At the start of Phase 02, before any design work begins.
**How to check:** Open the active spec and verify each item below.
**On failure:** Stop. List every failing item. Ask the user to address them before Phase 02 proceeds.

---

## 1. Artifact

- [ ] Spec file exists at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md`
- [ ] Spec status is `Draft` (not an unfilled template)

---

## 2. Completeness

Each section below must be filled in — not a placeholder, not the template's italic hint text.

- [ ] **Problem Statement** — at least one paragraph explaining the user pain or system gap
- [ ] **Goals** — at least one goal listed
- [ ] **Non-Goals** — at least one non-goal listed with a reason it is out of scope
- [ ] **User Stories** — at least two stories in `As a / I want / so that` format
- [ ] **Acceptance Criteria** — at least two rows in the AC table (AC-1, AC-2, ...)
- [ ] **Constraints** — at least one constraint documented (any category)

---

## 3. Quality

- [ ] Each acceptance criterion is verifiable — no vague terms (`fast`, `easy`, `user-friendly`) without a measurable threshold
- [ ] No user story is compound — a single story should not cover two independent user goals joined by "and"
- [ ] Acceptance criteria reference the user stories they validate (either by numbering or by clear subject match)

---

## 4. Blockers

- [ ] Open Questions table has no unresolved entries marked as blockers
- [ ] No requirement is too ambiguous to derive a design from (if so, add it to Open Questions and resolve it first)

---

## Gate Result

**Pass** — all items checked → proceed to Phase 02.

**Fail** — one or more items unchecked → do not start design. Report the failing items to the user with a brief explanation of what is missing, then stop.
