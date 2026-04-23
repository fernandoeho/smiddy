# Phase 05 — Review

**Input:** Implementation and tests from Phases 03–04. Spec at `.smiddy/specs/<feature-name>.md`.
**Output:** A written review report. Either an approval or a list of blocking and non-blocking issues.

**Requires:**
- `.smiddy/specs/architecture.md` — architectural consistency check
- `.smiddy/context/decisions.md` — standing decisions that must not be violated
- `.smiddy/context/stack.md` — allowed technologies

---

## Instructions

You are operating as a **Reviewer**. Load the persona from `.smiddy/prompts/agents/reviewer.md` before proceeding.

Your job is to critically evaluate the work produced in Phases 03–04 against the spec, the architecture, and engineering quality standards. You are not implementing — you are auditing.

### Step 1 — Gather context

Read in order:
1. The active spec — particularly acceptance criteria, design decisions, and constraints
2. `.smiddy/specs/architecture.md` — check for architectural consistency
3. `.smiddy/context/decisions.md` — check that no standing decision was violated
4. `.smiddy/context/stack.md` — check that only allowed technologies were used

### Step 2 — Review correctness

For each acceptance criterion in the spec:
- Does the implementation satisfy it?
- Is there a test that verifies it?
- Does the test actually fail when the implementation is broken?

Mark each AC as: Satisfied / Partially satisfied / Not satisfied.

### Step 3 — Review code quality

Evaluate each changed file against these dimensions:

| Dimension | Questions to ask |
|---|---|
| Clarity | Would a new team member understand this without a comment? |
| Simplicity | Is there a simpler way to achieve the same result? |
| Scope | Does any change go beyond what the spec required? |
| Conventions | Does the code match the style of surrounding code? |
| Duplication | Is logic duplicated that should be shared? |

### Step 4 — Review security

Check for OWASP Top 10 issues relevant to the change:
- Input validation at system boundaries
- Authentication and authorization on new endpoints or operations
- Injection vulnerabilities (SQL, command, template)
- Sensitive data exposure (secrets, PII in logs or responses)
- Insecure direct object references

### Step 5 — Review test quality

- Are tests testing behavior or implementation details?
- Are there edge cases in the acceptance criteria with no test coverage?
- Would the tests catch a regression if the implementation were changed?

### Step 6 — Write the review report

Structure your report as:

```
## Review Report: [feature name]

### Summary
[One paragraph: overall verdict and key findings]

### Acceptance Criteria Status
| AC | Status | Notes |
|---|---|---|
| AC-1 | Satisfied / Partial / Missing | |

### Blocking Issues
- [Issue]: [description and location] — must be resolved before approval

### Non-Blocking Issues
- [Issue]: [description and location] — recommended but not required

### Approval Decision
[ ] Approved
[ ] Approved with minor changes (non-blocking only)
[ ] Changes required (blocking issues present)
```

---

## Definition of Done for This Phase

- [ ] Every acceptance criterion evaluated and status recorded
- [ ] Security review completed
- [ ] Test quality evaluated
- [ ] Review report written with explicit approval decision
- [ ] All blocking issues described with enough detail to act on
- [ ] Spec status updated to Approved (if no blockers) or left In Review (if blockers exist)
