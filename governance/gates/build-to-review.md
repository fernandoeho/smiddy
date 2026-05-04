# Gate: Build → Review

**When to check:** At the start of Phase 04, before reviewing any code.
**How to check:** Open the spec, examine the implementation, and run the test suite.
**On failure:** Stop. List every failing item. Ask the user to complete Phase 03 before Phase 04 proceeds.

---

## 1. Artifact

- [ ] Spec file exists at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md`
- [ ] Spec status is `In Review`

---

## 2. Completeness

- [ ] Code changes exist — at least one file was modified or created to implement the feature
- [ ] At least one test file exists covering the new or changed code
- [ ] Every acceptance criterion in the spec has at least one corresponding test
- [ ] "Out-of-Scope Changes Discovered" section in the spec is present (even if empty)

---

## 3. Quality

- [ ] The full test suite passes — run it now and confirm; a failing test is a blocker regardless of whether it is new or pre-existing
- [ ] No acceptance criterion is explicitly unimplemented or marked as skipped
- [ ] No test is trivially empty (e.g., `assert True`, `pass`, no assertions)

---

## 4. Blockers

- [ ] Open Questions table has no unresolved entries that would invalidate the implementation
- [ ] No implementation decision was deferred that the spec required Phase 03 to make

---

## Gate Result

**Pass** — all items checked → proceed to Phase 04.

**Fail** — one or more items unchecked → do not start the review. Report the failing items to the user with a brief explanation of what is missing, then stop.
