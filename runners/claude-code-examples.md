# Claude Code — Phase Invocation Examples

Ready-to-paste prompts for running each Smiddy phase in a Claude Code session. Replace `my-feature` with your actual spec file name.

---

## Setup — Stack Discovery (existing projects, run once)

```
Read .smiddy/prompts/setup/stack-discovery.md and follow its instructions against this project.
```

---

## Load Context (start of each session)

```
Read and internalize: .smiddy/context/stack.md, .smiddy/context/decisions.md, .smiddy/context/glossary.md, .smiddy/specs/architecture.md
```

---

## Phase 01 — Requirements

```
Active spec: .smiddy/specs/my-feature.md

Read .smiddy/prompts/phases/01-requirements.md and follow its instructions.
The feature request is: [describe what needs to be built]
```

---

## Phase 02 — Design

```
Active spec: .smiddy/specs/my-feature.md

Read .smiddy/prompts/phases/02-design.md and follow its instructions.
```

With explicit persona loading:

```
Adopt the Architect persona from .smiddy/prompts/agents/architect.md, then run Phase 02 using spec: .smiddy/specs/my-feature.md
```

---

## Phase 03 — Implementation

```
Active spec: .smiddy/specs/my-feature.md

Read .smiddy/prompts/phases/03-implementation.md and follow its instructions.
```

---

## Phase 04 — Tests

```
Active spec: .smiddy/specs/my-feature.md

Read .smiddy/prompts/phases/04-tests.md and follow its instructions.
```

---

## Phase 05 — Review

```
Active spec: .smiddy/specs/my-feature.md

Read .smiddy/prompts/phases/05-review.md and follow its instructions.
```

---

## Phase 06 — Documentation

```
Active spec: .smiddy/specs/my-feature.md

Read .smiddy/prompts/phases/06-docs.md and follow its instructions.
```

---

## Full Autonomous Pipeline

```
Workflow: .smiddy/workflows/new-feature.md
Spec: .smiddy/specs/my-feature.md
Context: .smiddy/context/stack.md, .smiddy/context/decisions.md, .smiddy/context/glossary.md

Run all phases in sequence. Stop at each phase gate and confirm outputs before proceeding.
Do not advance past a phase until its Definition of Done is complete.
```

---

## Resume Mid-Pipeline

```
We completed Phase 03. Tests are not yet written. Resume from Phase 04 using spec: .smiddy/specs/my-feature.md
```

---

## Useful Modifiers

Force confirmation at every Definition of Done checklist:
```
Confirm each item in the Definition of Done checklist before proceeding to the next phase.
```

Restrict scope to the spec:
```
Only modify files listed in the Affected Components section of the spec.
```

Persist architecture decisions after Phase 02:
```
Append any new ADRs to .smiddy/context/decisions.md now.
```
