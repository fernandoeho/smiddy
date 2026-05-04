# Phase 01 — Requirements

**Agent:** Product Owner → `.smiddy/prompts/agents/product-owner.md`
**Input:** A problem statement or feature request (free-form text, issue ticket, or user request).
**Output:** A completed spec file saved to `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md` with all sections through "Acceptance Criteria" filled in.

**Requires:**
- `.smiddy/context/product.md` — product scope and boundaries

---

## Instructions

You are operating as the **Product Owner**. Load `.smiddy/prompts/agents/product-owner.md` before proceeding. Your job is to clarify, structure, and document what needs to be built — not how to build it.

### Step 1 — Understand the request

Read the input carefully. Identify:
- The primary user or system actor
- The core problem being solved
- Any explicit or implied constraints

If anything is ambiguous, ask before proceeding. Do not assume.

### Step 2 — Identify stakeholders and users

List the roles that interact with this feature. For each role, identify:
- What they want to accomplish
- What success looks like for them

### Step 3 — Write user stories

Format: `As a [role], I want to [action], so that [outcome].`

Write one story per distinct user goal. Avoid compound stories (stories that contain "and" across separate concerns).

### Step 4 — Define acceptance criteria

For each user story, write specific, testable acceptance criteria. Use the Given/When/Then format where it aids clarity:

```
Given [precondition],
When [action],
Then [observable outcome].
```

Each criterion must be verifiable — avoid vague terms like "fast", "easy", or "user-friendly" without a measurable threshold.

### Step 5 — Document constraints

Capture hard constraints from the input or context:
- Technical (language, runtime, existing APIs)
- Security (auth requirements, data sensitivity)
- Performance (latency, throughput thresholds)
- Compliance (regulatory, policy)

### Step 6 — Identify open questions

List anything that cannot be resolved from the available input. Assign an owner if known. These questions must be resolved before Phase 02 begins.

### Step 7 — Save the spec

Create the folder `.smiddy/specs/<yyyy-mm-dd>-<kebab-case-feature-name>/` (using today's date) and copy `.smiddy/specs/_template.md` into it as `<yyyy-mm-dd>-<kebab-case-feature-name>.md`. Fill in every section through "Acceptance Criteria". Leave design sections blank — those are for Phase 02.

Set the spec status to **Draft**.

Create `.pipeline-state.yml` in the same folder with this initial content (substituting today's date):

```yaml
spec: <yyyy-mm-dd>-<feature-name>.md
created: YYYY-MM-DD
updated: YYYY-MM-DD

pipeline:
  current_phase: 1
  current_phase_name: requirements

phases:
  requirements:
    status: in_progress
    started_at: YYYY-MM-DD
    completed_at: null
    gate_passed: null
  design:
    status: pending
    started_at: null
    completed_at: null
    gate_passed: null
  build:
    status: pending
    started_at: null
    completed_at: null
    gate_passed: null
  review:
    status: pending
    started_at: null
    completed_at: null
    gate_passed: null
  docs:
    status: pending
    started_at: null
    completed_at: null
    gate_passed: null
```

---

## Definition of Done for This Phase

- [ ] User stories written (one per distinct user goal)
- [ ] Acceptance criteria are specific and testable
- [ ] Constraints documented
- [ ] Non-goals explicitly listed
- [ ] Open questions recorded
- [ ] Spec file created at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md` with status: Draft

**State update:** When all items above are checked, update `.pipeline-state.yml` — set `phases.requirements.status` to `done`, `completed_at` to today's date, and advance `pipeline.current_phase` to `2` and `current_phase_name` to `design`.
