# Gate: Review → Docs

**When to check:** At the start of Phase 05, before writing any documentation.
**How to check:** Locate the Phase 04 review report and verify each item below.
**On failure:** Stop. List every failing item. Ask the user to complete Phase 04 before Phase 05 proceeds.

---

## 1. Artifact

- [ ] A written review report exists for this feature (inline in the conversation or saved to the spec)
- [ ] Spec status is `Approved` — not `Draft`, `In Review`, or missing

---

## 2. Completeness

- [ ] Every acceptance criterion has a recorded status: Satisfied / Partially satisfied / Not satisfied
- [ ] Blocking Issues section is present (even if empty)
- [ ] Non-Blocking Issues section is present (even if empty)
- [ ] Standards Candidates section is present with at least one named candidate or the explicit text "None"

---

## 3. Quality

This gate's critical check: **the approval decision must not have blocking issues.**

- [ ] Approval decision is `Approved` or `Approved with minor changes` — a decision of `Changes required` blocks this gate entirely
- [ ] All blocking issues listed in the report have been resolved before this gate is checked (if any existed)
- [ ] Each blocking issue that was raised includes enough detail to verify it was actually addressed

---

## 4. Blockers

- [ ] No acceptance criterion has a status of `Not satisfied` without a corresponding resolved blocking issue
- [ ] No security finding from the review is unaddressed

---

## Gate Result

**Pass** — all items checked → proceed to Phase 05.

**Fail** — one or more items unchecked → do not start documentation. If the approval decision is `Changes required`, route back to Phase 03 to address the blocking issues, then re-run Phase 04. Report the failing items to the user, then stop.
