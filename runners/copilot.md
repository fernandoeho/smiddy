# Runner: GitHub Copilot

This guide explains how to invoke the Smiddy pipeline using GitHub Copilot in VS Code. It covers only tool-specific invocation — all pipeline logic lives in the phase prompts and workflows.

---

## Prerequisites

- GitHub Copilot extension installed and signed in
- Copilot Chat enabled (VS Code sidebar or inline chat)
- `.copilot/instructions.md` present in the project root (it is — Smiddy created it)
- `.smiddy/context/stack.md` filled in with your project's details

---

## How Copilot Reads Smiddy Instructions

GitHub Copilot reads `.copilot/instructions.md` automatically when it is present in the workspace root. This file loads the Smiddy operating constraints into Copilot's context for all chat interactions in this workspace.

No additional setup is required for the instructions to take effect.

---

## Running a Phase with Copilot Chat

Open the Copilot Chat sidebar (`Ctrl+Alt+I` / `Cmd+Option+I`).

For each phase, reference the active spec and the phase prompt file by attaching them or quoting the path:

**Example — starting Phase 01:**
```
@workspace
Active spec: .smiddy/specs/my-feature.md
Phase prompt: .smiddy/prompts/phases/01-requirements.md

Run Phase 01 against the input below:
[paste the feature request or problem statement]
```

**Example — running Phase 03 with Developer persona:**
```
@workspace
Spec: .smiddy/specs/my-feature.md
Persona: .smiddy/prompts/agents/developer.md
Phase: .smiddy/prompts/phases/03-implementation.md

Implement the changes described in the spec.
```

---

## Attaching Files

Copilot Chat supports attaching workspace files for context. Use the paperclip icon or `#file:` syntax to include relevant files without pasting their full contents:

```
#file:.smiddy/specs/my-feature.md
#file:.smiddy/context/stack.md
#file:.smiddy/prompts/phases/02-design.md
```

Attach only the files relevant to the current phase to avoid unnecessary context.

---

## Inline Chat for Phase 03 (Implementation)

For implementation, inline chat (`Ctrl+I` / `Cmd+I`) is effective for targeted edits:

1. Navigate to the file being changed.
2. Select the relevant code or place the cursor at the insertion point.
3. Open inline chat and describe the change in terms of the acceptance criterion:
   ```
   Implement AC-2 from .smiddy/specs/my-feature.md: [paste the criterion]
   ```

This keeps implementation focused on one criterion at a time.

---

## Manual Phase Advancement

Unlike Claude Code, Copilot does not advance phases autonomously. You drive the workflow manually:

1. Open `.smiddy/workflows/new-feature.md` (or the relevant workflow) as a checklist.
2. Work through each phase checklist item in Copilot Chat.
3. Check off items as they are completed.
4. Move to the next phase only when the current phase's Definition of Done is fully satisfied.

---

## Limitations to Work Around

| Limitation | Workaround |
|---|---|
| Context window fills up in long sessions | Start a new Copilot Chat window; re-attach spec and phase prompt |
| Copilot modifies files outside scope | Specify: "Only modify files listed in the Affected Components section of the spec" |
| Copilot adds speculative features | Specify: "Implement only what is required by the acceptance criteria, nothing more" |
| Copilot cannot run shell commands | Run test suite, linter, and type checker manually and paste output back into chat |

---

## Persisting Decisions

After Phase 02, manually copy any ADRs Copilot generates into `.smiddy/context/decisions.md`. Copilot does not write files autonomously — you must apply its suggestions using the VS Code diff editor or inline chat suggestions.

---

## Tips

- Use `@workspace` in Copilot Chat to give it access to the full project structure.
- Attach `.smiddy/context/decisions.md` to any chat involving architecture to prevent contradicting standing decisions.
- For review (Phase 05), open the changed files side-by-side with the spec and ask Copilot to evaluate each acceptance criterion one at a time.
