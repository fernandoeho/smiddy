# Runner: Claude Code

This guide explains how to invoke the Smiddy pipeline using Claude Code. It covers only tool-specific invocation — all pipeline logic lives in the phase prompts.

---

## Prerequisites

- Claude Code installed and authenticated (`claude --version`)
- `.smiddy/context/stack.md` filled in (run the stack discovery prompt below if starting from an existing project)
- A spec file created under `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/` (copy from `.smiddy/specs/_template.md`)

---

## Discovering Context (Existing Projects)

If you installed Smiddy into a project that already has code, run these two discovery prompts once before starting any pipeline phase.

**Stack discovery** — scans config files and dependencies:
```
Read .smiddy/prompts/setup/stack-discovery.md and follow its instructions against this project.
```

**Architecture discovery** — scans source code for component structure and data flows:
```
Read .smiddy/prompts/setup/architecture-discovery.md and follow its instructions against this project.
```

Run stack discovery first, then architecture discovery. Claude Code will write `.smiddy/context/stack.md` and `.smiddy/context/architecture.md` for you. Review each output and fill in anything it could not determine automatically.

> **New projects:** Skip architecture discovery. The Architect agent in Phase 02 will create `.smiddy/context/architecture.md` from scratch.

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
Active spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md

[paste contents of .smiddy/prompts/phases/01-requirements.md]
```

Claude Code will execute the phase, produce outputs, and stop at the Definition of Done checklist for your confirmation before advancing.

Phase 03 (Build) covers both implementation and tests. Claude Code will write production code, write the test suite, run the full suite, and confirm all tests pass before completing the phase.

---

## Running a Full Autonomous Pipeline

To run multiple phases autonomously without manual advancement, provide the full workflow context upfront:

```
Spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
Context: .smiddy/context/stack.md, .smiddy/context/decisions.md, .smiddy/context/glossary.md

Run all phases in sequence. Stop at each phase gate and confirm outputs before proceeding.
Do not advance past a phase until its Definition of Done is complete.
```

Claude Code will pause at each gate and report what was produced before continuing.

---

## Useful Patterns

**Loading context per phase:**
Each phase prompt declares its required files in a `Requires:` block. Load only those files before running the phase — do not load all context files up front. Example for Phase 02:

```
Read .smiddy/context/architecture.md, .smiddy/context/stack.md, .smiddy/context/decisions.md, then run Phase 02 using spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
```

**Resuming mid-pipeline:**
If a session was interrupted, tell Claude Code where you left off:

```
We completed Phase 03. Resume from Phase 04 using spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
```

**Assigning an agent persona:**
When a phase requires a specific agent, load the persona explicitly:

```
Adopt the Architect persona from .smiddy/prompts/agents/architect.md and run Phase 02.
```

---

## Shell Access

Claude Code has shell access and will use it during:
- Phase 04: running the test suite
- Phase 04: running type checks and linting
- Phase 05: building documentation artifacts

If a shell command requires confirmation, Claude Code will ask before running it.

---

## Persisting Decisions

Claude Code does not persist memory between sessions automatically. After Phase 02, ensure any ADRs are written to `.smiddy/context/decisions.md`. At the start of a new session, load that file explicitly so prior decisions are respected.

---

## Troubleshooting

| Symptom | Resolution |
|---|---|
| Claude Code ignores the spec | Paste the spec contents directly, or reference it with `Read file: .smiddy/specs/<yyyy-mm-dd>-<name>/<yyyy-mm-dd>-<name>.md` |
| Phase advances without completing DoD | Add "Confirm each item in the Definition of Done checklist before proceeding" to your prompt |
| Out-of-scope changes being made | Remind: "Only modify files listed in the spec's Affected Components section" |
| ADRs not being written | Explicitly instruct: "Append any new ADRs to .smiddy/context/decisions.md now" |
