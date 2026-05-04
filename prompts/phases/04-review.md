# Phase 04 — Review

**Input:** Implementation and tests from Phase 03. Spec at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md`.
**Output:** A written review report. Either an approval or a list of blocking and non-blocking issues.

**Requires:**
- `.smiddy/context/architecture.md` — architectural consistency check
- `.smiddy/governance/decisions/index.yml` — index of standing architectural decisions
- `.smiddy/context/stack.md` — allowed technologies
- `.smiddy/governance/standards/index.yml` — existing standards to check compliance against (if populated)

---

## Gate Check

Before reviewing any code, run the gate at `.smiddy/governance/gates/build-to-review.md` against the active spec.

If the gate **passes**: update `.pipeline-state.yml` — set `phases.review.status` to `in_progress`, `started_at` to today's date, `phases.build.gate_passed` to `true`, and `pipeline.current_phase_name` to `review`.

If the gate **fails**: update `.pipeline-state.yml` — set `phases.build.status` to `blocked` and `phases.build.gate_passed` to `false`. Report each failing item to the user and do not proceed until they are resolved.

---

## Instructions

You are operating as a **Reviewer**. Load the persona from `.smiddy/prompts/agents/reviewer.md` before proceeding.

Your job is to critically evaluate the work produced in Phase 03 against the spec, the architecture, and engineering quality standards. You are not implementing — you are auditing.

### Step 1 — Gather context

Read in order:
1. The active spec — particularly acceptance criteria, design decisions, and constraints
2. `.smiddy/context/architecture.md` — check for architectural consistency
3. `.smiddy/governance/decisions/index.yml` — scan area tags to identify ADRs relevant to what changed; read only those ADR files from `.smiddy/governance/decisions/`
4. `.smiddy/context/stack.md` — check that only allowed technologies were used
5. `.smiddy/governance/standards/index.yml` — if populated, identify and read standards relevant to what was changed

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

### Step 6 — Flag standard candidates

While reviewing the code, watch for patterns introduced or confirmed by this feature that are worth preserving as standards. A good candidate is:

- **New and reusable** — a pattern the Developer established that other features should follow
- **Non-obvious** — something a future agent or new developer would not know without being told
- **Consistent** — already applied correctly across the new code, not a one-off

Do not flag patterns that are already in `.smiddy/governance/standards/index.yml`, are standard framework behavior, or are obvious from the tooling.

For each candidate, note:
- A short name
- The pattern in one sentence
- 1–2 example locations in the code

These will be written as standards in Phase 05. If there are no candidates, record "None."

### Step 7 — Write the review report

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

### Standards Candidates
- [Name]: [one-sentence description] — see [file:line]
(or "None")

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
- [ ] Standards candidates identified (or explicitly recorded as "None")
- [ ] Review report written with explicit approval decision
- [ ] All blocking issues described with enough detail to act on
- [ ] Spec status updated to Approved (if no blockers) or left In Review (if blockers exist)

**State update:** When all items above are checked, update `.pipeline-state.yml` — set `phases.review.status` to `done`, `completed_at` to today's date, and advance `pipeline.current_phase` to `5` and `current_phase_name` to `docs`. If the approval decision was `Changes required`, instead set `phases.review.status` to `blocked` and reset `pipeline.current_phase` to `3` and `current_phase_name` to `build`.
