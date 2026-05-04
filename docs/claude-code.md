# Smiddy with Claude Code

How to invoke the Smiddy pipeline using Claude Code. All pipeline logic lives in the phase prompts — this file covers tool-specific invocation only.

---

## Prerequisites

- Claude Code installed and authenticated (`claude --version`)
- `.smiddy/context/stack.md` filled in (run the stack discovery prompt below if starting from an existing project)
- A spec file created under `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/` (copy from `.smiddy/specs/_template.md`)

---

## Discovering Context (Existing Projects)

Run these two prompts once before starting any pipeline phase.

**Stack discovery:**
```
Read .smiddy/prompts/setup/stack-discovery.md and follow its instructions against this project.
```

**Architecture discovery** (run after stack discovery):
```
Read .smiddy/prompts/setup/architecture-discovery.md and follow its instructions against this project.
```

Claude Code will write `.smiddy/context/stack.md` and `.smiddy/context/architecture.md`. Review each output and fill in anything it could not determine automatically.

> **New projects:** Skip architecture discovery. The Architect agent in Phase 02 creates `.smiddy/context/architecture.md` from scratch.

---

## Starting a Session

```
claude
```

Claude Code reads `.claude/CLAUDE.md` automatically at startup, which loads the Smiddy operating instructions.

---

## Running a Phase

Paste the phase prompt into the session, preceded by the active spec path. Example for Phase 01:

```
Active spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md

Read .smiddy/prompts/phases/01-requirements.md and follow its instructions.
The feature request is: [describe what needs to be built]
```

**Phase 02 — Design:**
```
Active spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md

Read .smiddy/prompts/phases/02-design.md and follow its instructions.
```

With explicit persona loading:
```
Adopt the Architect persona from .smiddy/prompts/agents/architect.md, then run Phase 02 using spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
```

**Phase 03 — Build:**
```
Active spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md

Read .smiddy/prompts/phases/03-build.md and follow its instructions.
```

**Phase 04 — Review:**
```
Active spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md

Read .smiddy/prompts/phases/04-review.md and follow its instructions.
```

**Phase 05 — Documentation:**
```
Active spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md

Read .smiddy/prompts/phases/05-docs.md and follow its instructions.
```

---

## Full Autonomous Pipeline

```
Spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md

Run all phases in sequence. For each phase, read the phase prompt and load the files listed in its Requires block before proceeding. Stop at each phase gate and confirm outputs before advancing.
Do not advance past a phase until its Definition of Done is complete.
```

---

## Resuming Mid-Pipeline

```
We completed Phase 03. Resume from Phase 04 using spec: .smiddy/specs/yyyy-mm-dd-my-feature/yyyy-mm-dd-my-feature.md
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
Write any new ADRs to .smiddy/decisions/ and update .smiddy/decisions/index.yml now.
```

---

## Shell Access

Claude Code has shell access and uses it during:
- Phase 03: running the test suite
- Phase 04: running type checks and linting
- Phase 05: building documentation artifacts

---

## Persisting Decisions

Claude Code does not persist memory between sessions. After Phase 02, ensure ADRs are written to `.smiddy/decisions/` and the index is updated. Load `.smiddy/decisions/index.yml` explicitly at the start of new sessions so prior decisions are respected.

---

## Troubleshooting

| Symptom | Resolution |
|---|---|
| Claude Code ignores the spec | Paste the spec contents directly, or reference it with `Read file: .smiddy/specs/<name>/<name>.md` |
| Phase advances without completing DoD | Add "Confirm each item in the Definition of Done checklist before proceeding" to your prompt |
| Out-of-scope changes being made | Remind: "Only modify files listed in the spec's Affected Components section" |
| ADRs not being written | Explicitly instruct: "Write any new ADRs to .smiddy/decisions/ and update .smiddy/decisions/index.yml now" |
