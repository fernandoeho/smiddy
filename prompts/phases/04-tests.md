# Phase 04 — Tests

**Input:** Completed implementation from Phase 03. Spec at `.smiddy/specs/<feature-name>.md`.
**Output:** Test files that verify all acceptance criteria. All tests passing.

**Requires:**
- `.smiddy/context/stack.md` — test framework and tooling conventions

---

## Instructions

You are operating as a **Developer** writing tests. Load the persona from `.smiddy/prompts/agents/developer.md` before proceeding.

Your job is to write tests that verify the production code from Phase 03 satisfies every acceptance criterion. Do not modify production code in this phase — if a test exposes a defect, note it and fix the production code first, then re-run.

### Step 1 — Map acceptance criteria to test cases

For each acceptance criterion in the spec, write down:
- The scenario being tested
- The test type (unit, integration, end-to-end)
- The expected observable outcome

No acceptance criterion should be untested. If a criterion cannot be tested automatically, document why and describe the manual verification procedure.

### Step 2 — Choose the right test type

| Test type | Use when |
|---|---|
| Unit | Testing a single function or class in isolation |
| Integration | Testing the interaction between two or more components |
| End-to-end | Testing a complete user-facing flow |

Prefer the lowest-cost test type that gives meaningful coverage. Do not write end-to-end tests for logic that can be covered by units.

### Step 3 — Write tests

Follow these rules:

**Clarity**
- Each test verifies one thing. One assertion per test where practical.
- Test names describe what is being tested and what outcome is expected.
- Do not test implementation details — test observable behavior.

**Isolation**
- Unit tests must not depend on real external services, databases, or filesystems.
- Use fakes or in-memory implementations over mocks where possible. Mocks tie tests to implementation details.

**Coverage**
- Cover the happy path.
- Cover each distinct error or edge case listed in the acceptance criteria.
- Cover boundary conditions if the spec mentions thresholds or limits.

**Maintenance**
- Do not duplicate setup across tests — use fixtures or helpers.
- Do not write tests that pass by coincidence (e.g., relying on global state or test execution order).

### Step 4 — Run the full suite

Run the project's test suite. All tests — not just new ones — must pass before this phase is complete. A regression in an existing test is a blocker.

### Step 5 — Report coverage

If the project has a coverage tool configured, run it and record the output. Note any acceptance criteria that have low or no coverage and explain why.

---

## Definition of Done for This Phase

- [ ] Every acceptance criterion has at least one automated test
- [ ] All tests pass (new and existing)
- [ ] No production code changed (defects go back to Phase 03)
- [ ] Test names clearly describe the scenario and expected outcome
- [ ] Coverage report reviewed (if tooling is configured)
- [ ] Any untestable criteria have documented manual procedures
