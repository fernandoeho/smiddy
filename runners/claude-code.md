# Runner: Claude Code

This guide explains how to invoke the Smiddy pipeline using Claude Code. It covers only tool-specific invocation — all pipeline logic lives in the phase prompts and workflows.

---

## Prerequisites

- Claude Code installed and authenticated (`claude --version`)
- Project cloned and `context/stack.md` filled in
- A spec file created under `specs/` (copy from `specs/_template.md`)

---

## Starting a Pipeline Session

Open a terminal in the project root and start Claude Code:

```
claude
```

At the start of every session, Claude Code will read `.claude/CLAUDE.md` automatically. This loads the Smiddy operating instructions.

---

## Running a Phase

For each phase, paste the phase prompt into the Claude Code session, preceded by the active spec path. Example for Phase 01:

```
Active spec: specs/my-feature.md

[paste contents of prompts/phases/01-requirements.md]
```

Claude Code will execute the phase, produce outputs, and stop at the Definition of Done checklist for your confirmation before advancing.

---

## Running a Full Autonomous Pipeline

To run multiple phases autonomously without manual advancement, provide the full workflow context upfront:

```
Workflow: workflows/new-feature.md
Spec: specs/my-feature.md
Context: context/stack.md, context/decisions.md, context/glossary.md

Run all phases in sequence. Stop at each phase gate and confirm outputs before proceeding.
Do not advance past a phase until its Definition of Done is complete.
```

Claude Code will pause at each gate and report what was produced before continuing.

---

## Useful Patterns

**Loading context once per session:**
At the start of a session, you can load all context files explicitly so they remain in the context window:

```
Read and internalize: context/stack.md, context/decisions.md, context/glossary.md, specs/architecture.md
```

**Resuming mid-pipeline:**
If a session was interrupted, tell Claude Code where you left off:

```
We completed Phase 03. Tests are not yet written. Resume from Phase 04 using spec: specs/my-feature.md
```

**Assigning an agent persona:**
When a phase requires a specific agent, load the persona explicitly:

```
Adopt the Architect persona from prompts/agents/architect.md and run Phase 02.
```

---

## Shell Access

Claude Code has shell access and will use it during:
- Phase 04: running the test suite
- Phase 05: running type checks and linting
- Phase 06: building documentation artifacts

If a shell command requires confirmation, Claude Code will ask before running it.

---

## Persisting Decisions

Claude Code does not persist memory between sessions automatically. After Phase 02, ensure any ADRs are written to `context/decisions.md`. At the start of a new session, load that file explicitly so prior decisions are respected.

---

## Troubleshooting

| Symptom | Resolution |
|---|---|
| Claude Code ignores the spec | Paste the spec contents directly, or reference it with `Read file: specs/<name>.md` |
| Phase advances without completing DoD | Add "Confirm each item in the Definition of Done checklist before proceeding" to your prompt |
| Out-of-scope changes being made | Remind: "Only modify files listed in the spec's Affected Components section" |
| ADRs not being written | Explicitly instruct: "Append any new ADRs to context/decisions.md now" |
