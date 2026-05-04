# Phase 02 — Design

**Input:** Approved spec file at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md` (status: Draft or In Review).
**Output:** Completed design sections in the spec, plus any new ADR files in `decisions/` and updated `decisions/index.yml`.

**Requires:**
- `.smiddy/context/architecture.md` — existing system shape
- `.smiddy/context/stack.md` — allowed tech stack
- `.smiddy/decisions/index.yml` — index of standing architectural decisions
- `.smiddy/standards/index.yml` — project coding standards (if populated)

---

## Instructions

You are operating as an **Architect**. Load the persona from `.smiddy/prompts/agents/architect.md` before proceeding.

Your job is to decide *how* the system will be built to satisfy the requirements — not to write implementation code.

### Step 1 — Review inputs

Read in order:
1. The active spec at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md`
2. `.smiddy/context/architecture.md` — understand the existing system shape
3. `.smiddy/context/stack.md` — confirm the allowed tech stack
4. `.smiddy/decisions/index.yml` — scan area tags to identify ADRs relevant to the components being modified; read only those ADR files from `.smiddy/decisions/`
5. `.smiddy/standards/index.yml` — if it contains entries, identify and read standards relevant to the components being modified

Do not propose designs that contradict standing decisions unless you explicitly surface a new ADR. Do not propose interface contracts that contradict a documented standard without flagging it.

### Step 2 — Identify affected components

List every existing component that will change and every new component that will be created. For each, describe:
- What responsibility it gains, loses, or retains
- Whether its public interface changes

### Step 3 — Define interface contracts

For every new or changed interface (API endpoint, function signature, event schema, message format):
- Write the contract explicitly (name, inputs, outputs, errors)
- Do not leave contracts implicit or described only in prose

### Step 4 — Design the data model

If persistent data is created or modified:
- Define the schema changes
- Describe the migration strategy (if applicable)
- Identify any index, constraint, or performance considerations

### Step 5 — Evaluate alternatives

For each significant design decision, briefly state:
- The option chosen
- One or two alternatives considered
- Why the chosen option wins

If a decision is architecturally significant (affects multiple components, is hard to reverse, or has compliance implications):
1. Create `.smiddy/decisions/ADR-NNN-short-title.md` using the format in `.smiddy/decisions/README.md`
2. Add an entry to `.smiddy/decisions/index.yml` with appropriate area tags so future phases can find it

### Step 6 — Update the spec

Fill in the "Proposed Design", "Affected Components", "Interface Contracts", and "Data Model Changes" sections of the spec. Update spec status to **In Review**.

### Step 7 — Surface open questions

If any requirement is under-specified for design purposes, add it to the spec's "Open Questions" section. Do not proceed past this phase until blockers are resolved.

---

## Definition of Done for This Phase

- [ ] Affected components listed with change types
- [ ] All interface contracts defined explicitly
- [ ] Data model changes documented with migration plan
- [ ] Design alternatives evaluated for significant decisions
- [ ] New ADR files written in `.smiddy/decisions/` and index updated
- [ ] Spec updated and status set to In Review
