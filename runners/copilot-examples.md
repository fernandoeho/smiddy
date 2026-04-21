# GitHub Copilot — Phase Invocation Examples

Ready-to-paste prompts for running each Smiddy phase in Copilot Chat. Replace `my-feature` with your actual spec file name.

Open Copilot Chat with `Cmd+Option+I` (Mac) or `Ctrl+Alt+I` (Windows/Linux).

---

## Setup — Stack Discovery (existing projects, run once)

```
@workspace
#file:.smiddy/prompts/setup/stack-discovery.md

Follow the instructions in this file against the current project.
```

---

## Load Context (start of each session)

```
@workspace
#file:.smiddy/context/stack.md
#file:.smiddy/context/decisions.md
#file:.smiddy/context/glossary.md
#file:.smiddy/specs/architecture.md

Internalize these files. They are the context for all phases in this session.
```

---

## Phase 01 — Requirements

```
@workspace
#file:.smiddy/specs/my-feature.md
#file:.smiddy/prompts/phases/01-requirements.md
#file:.smiddy/prompts/agents/product-owner.md

Run Phase 01 against the following feature request:
[describe what needs to be built]
```

---

## Phase 02 — Design

```
@workspace
#file:.smiddy/specs/my-feature.md
#file:.smiddy/prompts/phases/02-design.md
#file:.smiddy/prompts/agents/architect.md
#file:.smiddy/context/stack.md
#file:.smiddy/context/decisions.md

Run Phase 02. Follow the instructions in the phase prompt.
```

---

## Phase 03 — Implementation

```
@workspace
#file:.smiddy/specs/my-feature.md
#file:.smiddy/prompts/phases/03-implementation.md
#file:.smiddy/prompts/agents/developer.md
#file:.smiddy/context/stack.md

Run Phase 03. Implement only what is required by the acceptance criteria.
```

For targeted inline edits, use inline chat (`Cmd+I` / `Ctrl+I`) on the relevant file:

```
Implement AC-2 from .smiddy/specs/my-feature.md: [paste the criterion]
```

---

## Phase 04 — Tests

```
@workspace
#file:.smiddy/specs/my-feature.md
#file:.smiddy/prompts/phases/04-tests.md
#file:.smiddy/prompts/agents/developer.md

Run Phase 04. Write tests for every acceptance criterion in the spec.
```

---

## Phase 05 — Review

```
@workspace
#file:.smiddy/specs/my-feature.md
#file:.smiddy/prompts/phases/05-review.md
#file:.smiddy/prompts/agents/reviewer.md
#file:.smiddy/context/decisions.md

Run Phase 05. Evaluate the implementation against the spec and report any blocking issues.
```

---

## Phase 06 — Documentation

```
@workspace
#file:.smiddy/specs/my-feature.md
#file:.smiddy/prompts/phases/06-docs.md

Run Phase 06. Update documentation for all changes made in this pipeline run.
```

---

## Resume Mid-Pipeline

```
@workspace
#file:.smiddy/specs/my-feature.md
#file:.smiddy/prompts/phases/04-tests.md
#file:.smiddy/prompts/agents/developer.md

We completed Phase 03. Resume from Phase 04.
```

---

## Useful Modifiers

Restrict scope to the spec:
```
Only modify files listed in the Affected Components section of the spec.
```

Prevent speculative additions:
```
Implement only what is required by the acceptance criteria, nothing more.
```

Persist architecture decisions after Phase 02:
```
List all ADRs produced in this session so I can append them to .smiddy/context/decisions.md
```

> Note: Copilot does not write files autonomously. Apply its suggestions using the VS Code diff editor or inline chat, then manually save ADRs to `.smiddy/context/decisions.md`.
