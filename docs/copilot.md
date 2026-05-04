# Smiddy with GitHub Copilot

How to invoke the Smiddy pipeline using GitHub Copilot in VS Code. All pipeline logic lives in the phase prompts — this file covers tool-specific invocation only.

Open Copilot Chat with `Cmd+Option+I` (Mac) or `Ctrl+Alt+I` (Windows/Linux).

---

## Prerequisites

- GitHub Copilot extension installed and signed in
- Copilot Chat enabled (VS Code sidebar or inline chat)
- `.copilot/instructions.md` present in the project root (Smiddy created it)
- `.smiddy/context/stack.md` filled in (see below if starting from an existing project)

---

## How Copilot Reads Smiddy Instructions

Copilot reads `.copilot/instructions.md` automatically when present in the workspace root. No additional setup is required.

---

## Discovering Context (Existing Projects)

Run these two prompts once in Copilot Chat before starting any pipeline phase.

**Stack discovery:**
```
@workspace
#file:.smiddy/prompts/setup/stack-discovery.md

Follow the instructions in this file against the current project.
```

**Architecture discovery** (run after stack discovery):
```
@workspace
#file:.smiddy/prompts/setup/architecture-discovery.md

Follow the instructions in this file against the current project.
```

Review each output and apply it using the VS Code diff editor. Fill in anything Copilot could not determine automatically.

> **New projects:** Skip architecture discovery. The Architect agent in Phase 02 creates `.smiddy/context/architecture.md` from scratch.

---

## Running a Phase

**Phase 01 — Requirements:**
```
@workspace
#file:.smiddy/context/product.md
#file:.smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
#file:.smiddy/prompts/phases/01-requirements.md
#file:.smiddy/prompts/agents/product-owner.md

Run Phase 01 against the following feature request:
[describe what needs to be built]
```

**Phase 02 — Design:**
```
@workspace
#file:.smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
#file:.smiddy/prompts/phases/02-design.md
#file:.smiddy/prompts/agents/architect.md
#file:.smiddy/context/architecture.md
#file:.smiddy/context/stack.md
#file:.smiddy/governance/decisions/index.yml

Run Phase 02. Follow the instructions in the phase prompt.
```

**Phase 03 — Build:**
```
@workspace
#file:.smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
#file:.smiddy/prompts/phases/03-build.md
#file:.smiddy/prompts/agents/developer.md
#file:.smiddy/context/stack.md

Run Phase 03. Implement all acceptance criteria and write tests for each one.
```

For targeted inline edits, use inline chat (`Cmd+I` / `Ctrl+I`) on the relevant file:
```
Implement AC-2 from .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md: [paste the criterion]
```

**Phase 04 — Review:**
```
@workspace
#file:.smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
#file:.smiddy/prompts/phases/04-review.md
#file:.smiddy/prompts/agents/reviewer.md
#file:.smiddy/context/architecture.md
#file:.smiddy/governance/decisions/index.yml
#file:.smiddy/context/stack.md

Run Phase 04. Evaluate the implementation against the spec and report any blocking issues.
```

**Phase 05 — Documentation:**
```
@workspace
#file:.smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
#file:.smiddy/prompts/phases/05-docs.md
#file:.smiddy/context/architecture.md

Run Phase 05. Update documentation for all changes made in this pipeline run.
```

---

## Resuming Mid-Pipeline

```
@workspace
#file:.smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
#file:.smiddy/prompts/phases/04-review.md
#file:.smiddy/prompts/agents/reviewer.md
#file:.smiddy/context/architecture.md
#file:.smiddy/governance/decisions/index.yml
#file:.smiddy/context/stack.md

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
List all ADRs produced in this session so I can write them to .smiddy/governance/decisions/ and update .smiddy/governance/decisions/index.yml
```

> Note: Copilot does not write files autonomously. Apply its suggestions using the VS Code diff editor or inline chat, then manually create ADR files in `.smiddy/governance/decisions/` and update `.smiddy/governance/decisions/index.yml`.

---

## Manual Phase Advancement

Unlike Claude Code, Copilot does not advance phases autonomously. You drive the workflow manually:

1. Work through each phase in Copilot Chat, following the phase prompts under `.smiddy/prompts/phases/`.
2. Phase 03 (Build) covers both implementation and tests — complete both before moving on.
3. Check off items as they are completed.
4. Move to the next phase only when the current phase's Definition of Done is fully satisfied.

---

## Limitations

| Limitation | Workaround |
|---|---|
| Context window fills up in long sessions | Start a new Copilot Chat window; re-attach spec and phase prompt |
| Copilot modifies files outside scope | Specify: "Only modify files listed in the Affected Components section of the spec" |
| Copilot adds speculative features | Specify: "Implement only what is required by the acceptance criteria, nothing more" |
| Copilot cannot run shell commands | Run test suite, linter, and type checker manually and paste output back into chat |
