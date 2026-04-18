# Workflow: Bug Fix

Use this workflow when correcting incorrect behavior in existing code.

---

## When to Use

- A feature does not behave as specified
- A runtime error or exception is occurring
- Data is being corrupted or lost
- A security vulnerability was discovered

## When Not to Use

- Building new capability → use `new-feature.md`
- Releasing a set of changes → use `release.md`

---

## Phase Sequence

Bug fixes use a compressed pipeline. Requirements and design are lightweight — the focus is on root cause analysis, a targeted fix, and a regression test.

```
01 Requirements (root cause) ──► 03 Implementation (fix) ──► 04 Tests (regression) ──► 05 Review ──► 06 Docs (if user-facing)
```

Phase 02 (Design) is **optional**. Include it if the fix requires structural changes.

---

## Phase 01 — Root Cause Analysis

Before writing any code, answer these questions in the spec:

1. **What is the observed behavior?** (exact, reproducible steps)
2. **What is the expected behavior?** (from spec, docs, or user expectation)
3. **Where does the failure originate?** (file, function, line if known)
4. **Why does it fail?** (root cause — not symptoms)
5. **What is the minimal change that would prevent this failure?**

Do not skip root cause analysis. Fixing symptoms instead of causes produces recurring bugs.

Write a minimal spec entry in `specs/<bug-name>.md` using the template. The "Problem Statement" and "Acceptance Criteria" are required. Design sections are optional unless structural changes are needed.

---

## Phase 02 — Design (optional)

Include this phase only if the fix requires:
- Changing component boundaries or interfaces
- Modifying a data model
- Introducing a new dependency

For a localized fix (single function or module), skip to Phase 03.

---

## Phase 03 — Implementation

Follow all rules from `prompts/phases/03-implementation.md` with these additions:

- **Fix the root cause, not the symptom.** If the root cause is in a different location than where the bug surfaces, fix it at the source.
- **Do not expand scope.** A bug fix should touch the minimum code necessary. Do not refactor while fixing.
- **Do not remove the failing case.** If there was a test that should have caught this, fix the test too — but do not simply delete a failing assertion.

---

## Phase 04 — Tests

Write a **regression test first** — a test that reproduces the bug against the pre-fix code and fails. Then apply the fix. Confirm the test passes.

This test must:
- Reproduce the exact failure scenario
- Fail without the fix
- Pass with the fix
- Continue to pass as the codebase evolves

---

## Phase 05 — Review

Same as the standard review phase. Reviewer must confirm:
- Root cause is addressed (not just symptoms)
- Regression test is present and meaningful
- No new issues introduced

---

## Phase 06 — Docs

Required only if:
- The bug was caused by a documentation error (update the docs)
- The fix changes user-visible behavior (add a changelog entry)
- The fix changes an API contract (update API docs)

---

## Checklist

- [ ] Root cause identified and documented
- [ ] Spec created at `specs/<bug-name>.md`
- [ ] Fix targets root cause, not symptom
- [ ] Regression test written and failing before fix
- [ ] All tests pass after fix
- [ ] Review approved
- [ ] Changelog updated if user-visible
- [ ] Spec status set to Done

---

## Branching Convention

```
fix/<kebab-case-bug-name>
```

Branch from `main`. For production hotfixes, branch from the release tag and cherry-pick to `main`.
