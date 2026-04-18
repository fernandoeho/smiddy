# Workflow: New Feature

Use this workflow when building a net-new capability that did not exist before.

---

## When to Use

- Adding a new user-facing feature
- Building a new internal service or component
- Introducing a new integration with an external system

## When Not to Use

- Fixing a defect → use `bug-fix.md`
- Shipping a versioned release → use `release.md`
- Refactoring without changing behavior → adapt Phase 03 only, skip 01–02 if spec already exists

---

## Phase Sequence

Run phases in order. Do not advance until the current phase's Definition of Done is complete.

```
01 Requirements ──► 02 Design ──► 03 Implementation ──► 04 Tests ──► 05 Review ──► 06 Docs
```

**Gates:**
- Do not start Phase 02 until the spec exists and open questions are resolved.
- Do not start Phase 03 until the design is reviewed and accepted.
- Do not start Phase 04 until production code is complete and stable.
- Do not start Phase 05 until all tests pass.
- Do not start Phase 06 until the review is Approved.

---

## Checklist

### Phase 01 — Requirements
- [ ] Problem statement understood
- [ ] User stories written
- [ ] Acceptance criteria defined and testable
- [ ] Constraints documented
- [ ] Non-goals listed
- [ ] Open questions recorded
- [ ] Spec created at `specs/<feature-name>.md` (status: Draft)

### Phase 02 — Design
- [ ] Affected components identified
- [ ] Interface contracts defined
- [ ] Data model changes documented
- [ ] Significant decisions recorded as ADRs in `context/decisions.md`
- [ ] Spec updated (status: In Review)

### Phase 03 — Implementation
- [ ] All acceptance criteria satisfiable by written code
- [ ] No test files written
- [ ] No out-of-spec features added
- [ ] Out-of-scope findings recorded in spec

### Phase 04 — Tests
- [ ] Every acceptance criterion has at least one test
- [ ] All tests (new and existing) pass
- [ ] No production code changed

### Phase 05 — Review
- [ ] All acceptance criteria verified: Satisfied / Partial / Missing
- [ ] Security review complete
- [ ] Review report written
- [ ] Approval decision: Approved / Changes Required

### Phase 06 — Docs
- [ ] Inline documentation written for new public interfaces
- [ ] Architecture docs updated if structure changed
- [ ] Changelog entry added
- [ ] README updated if setup or usage changed
- [ ] Spec status set to Done

---

## Branching Convention

```
feature/<kebab-case-spec-name>
```

Branch from `main`. Open a pull request targeting `main` after Phase 05 approval.
