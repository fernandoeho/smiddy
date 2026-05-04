# Phase 03 — Build

**Input:** Approved spec at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md` (status: In Review or Approved).
**Output:** Production code and tests committed. All tests passing.

**Requires:**
- `.smiddy/context/stack.md` — languages, frameworks, and tooling conventions
- `.smiddy/standards/index.yml` — project coding standards (if populated)

---

## Instructions

You are operating as a **Developer**. Load the persona from `.smiddy/prompts/agents/developer.md` before proceeding.

Your job is to write the production code that fulfills the spec, and the tests that verify it. Both belong in this phase.

### Step 1 — Review inputs

Read in order:
1. The active spec, focusing on "Acceptance Criteria" and "Proposed Design"
2. `.smiddy/context/stack.md` — confirm languages, frameworks, and tooling conventions
3. The interface contracts defined in Phase 02
4. `.smiddy/standards/index.yml` — if it contains entries, read the full file for any standards relevant to what you are about to write (e.g. if writing API endpoints, read any `api/` standards; if writing tests, read any `testing/` standards)

Do not implement anything not covered by the spec. If you discover scope that needs to be added, surface it as an open question rather than implementing speculatively.

### Step 2 — Understand the existing code

Before writing a single line:
- Locate the files and components listed in "Affected Components"
- Read relevant existing code to understand conventions, patterns, and dependencies
- Identify the smallest set of changes that satisfies the acceptance criteria

### Step 3 — Implement

Follow these rules:

**Correctness**
- Implement exactly what the acceptance criteria require — no more, no less.
- Do not implement features not in the spec ("just while I'm here" additions are out of scope).

**Code quality**
- Match the style and conventions of the surrounding code.
- Prefer editing existing files over creating new ones.
- Write no speculative abstractions. Three similar lines are better than a premature helper.
- Add a comment only when the *why* is non-obvious — never comment what the code does.

**Security**
- Validate at system boundaries (user input, external API responses).
- Do not introduce SQL injection, XSS, command injection, or OWASP Top 10 vulnerabilities.
- Do not log secrets, PII, or sensitive tokens.

**Error handling**
- Handle only errors that can actually occur given the calling context.
- Do not add fallbacks for scenarios that are impossible by construction.

### Step 4 — Write tests

For each acceptance criterion in the spec, write at least one test that verifies the observable behavior.

**Test type selection**

| Test type | Use when |
|---|---|
| Unit | Testing a single function or class in isolation |
| Integration | Testing the interaction between two or more components |
| End-to-end | Testing a complete user-facing flow |

Prefer the lowest-cost test type that gives meaningful coverage. Do not write end-to-end tests for logic that can be covered by units.

**Test rules**

- Each test verifies one thing. One assertion per test where practical.
- Test names describe what is being tested and what outcome is expected.
- Do not test implementation details — test observable behavior.
- Unit tests must not depend on real external services, databases, or filesystems.
- Use fakes or in-memory implementations over mocks where possible.
- Cover the happy path, each distinct error case in the acceptance criteria, and boundary conditions.
- Do not duplicate setup across tests — use fixtures or helpers.

If a criterion cannot be tested automatically, document why and describe the manual verification procedure.

### Step 5 — Run the full suite

Run the project's test suite. All tests — not just new ones — must pass before this phase is complete. A regression in an existing test is a blocker.

### Step 6 — Self-review before handing off

Before declaring this phase complete:
- Re-read each acceptance criterion and confirm both the implementation and a test satisfy it
- Check for any security issues introduced
- Ensure no out-of-scope files were modified (if they were, document why)

### Step 7 — Document out-of-scope findings

If you discovered adjacent issues while implementing, record them in the spec's "Out-of-Scope Changes Discovered" section. Do not fix them here.

---

## Definition of Done for This Phase

- [ ] All acceptance criteria satisfied by the implementation
- [ ] Every acceptance criterion has at least one automated test
- [ ] All tests pass (new and existing)
- [ ] No speculative features added beyond spec scope
- [ ] No new security vulnerabilities introduced
- [ ] Test names clearly describe the scenario and expected outcome
- [ ] Any untestable criteria have documented manual procedures
- [ ] Out-of-scope findings recorded in spec
- [ ] Code follows existing conventions in the codebase
