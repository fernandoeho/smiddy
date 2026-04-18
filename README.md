# Smiddy

**Tool-agnostic SDLC autonomous pipeline framework.**

Smiddy provides a structured, phase-driven pipeline for software development that runs on any AI coding assistant. All prompts and workflows are runtime-neutral — the runner layer is the only thing that changes when you switch tools.

---

## Tool Selection Guide

| Criterion | Claude Code | GitHub Copilot |
|---|---|---|
| Primary interface | Terminal / CLI | VS Code / IDE |
| Best for | Autonomous multi-step tasks | In-editor assistance |
| Context window | Very large | Moderate |
| Tool use / shell access | Native | Extension-dependent |
| Cost model | Per-token (Anthropic) | Subscription (GitHub) |
| Fine-tuned on your repo | No | Workspace indexing |

**Choose Claude Code if:** you want fully autonomous pipeline runs, large context tasks, or shell-integrated workflows.

**Choose GitHub Copilot if:** your team lives in VS Code, prefers inline suggestions, or is already on a GitHub Enterprise plan.

You can use both simultaneously — Claude Code for pipeline orchestration, Copilot for in-editor autocomplete.

---

## Project Structure

```
smiddy/
├── README.md                  # This file
├── .claude/
│   └── CLAUDE.md              # Claude Code adapter
├── .copilot/
│   └── instructions.md        # GitHub Copilot adapter
├── specs/
│   ├── _template.md           # Spec authoring template
│   └── architecture.md        # System architecture
├── prompts/
│   ├── phases/
│   │   ├── 01-requirements.md
│   │   ├── 02-design.md
│   │   ├── 03-implementation.md
│   │   ├── 04-tests.md
│   │   ├── 05-review.md
│   │   └── 06-docs.md
│   └── agents/
│       ├── architect.md
│       ├── developer.md
│       └── reviewer.md
├── workflows/
│   ├── new-feature.md
│   ├── bug-fix.md
│   └── release.md
├── context/
│   ├── stack.md
│   ├── decisions.md
│   └── glossary.md
└── runners/
    ├── claude-code.md
    └── copilot.md
```

---

## Quick Start

1. **Fill in context** — edit `context/stack.md`, `context/decisions.md`, and `context/glossary.md` with your project's specifics.
2. **Write a spec** — copy `specs/_template.md`, fill it in, save as `specs/<feature-name>.md`.
3. **Pick a workflow** — open the relevant file in `workflows/`.
4. **Pick a runner** — open `runners/claude-code.md` or `runners/copilot.md` for tool-specific invocation instructions.
5. **Run the pipeline** — follow the phase sequence in the workflow, feeding each phase prompt to your chosen AI tool.

---

## Pipeline Phases

| Phase | Prompt | Output |
|---|---|---|
| 01 Requirements | `prompts/phases/01-requirements.md` | Acceptance criteria, constraints |
| 02 Design | `prompts/phases/02-design.md` | Architecture decisions, interfaces |
| 03 Implementation | `prompts/phases/03-implementation.md` | Working code |
| 04 Tests | `prompts/phases/04-tests.md` | Test suite |
| 05 Review | `prompts/phases/05-review.md` | Review report |
| 06 Docs | `prompts/phases/06-docs.md` | Documentation |

Phases are sequential by default. You may skip phases or run subsets depending on the workflow.

---

## How It Works

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                          SMIDDY FRAMEWORK                           │
│                                                                     │
│  ┌──────────────┐    ┌──────────────────────────────────────────┐  │
│  │   CONTEXT    │    │               PIPELINE                   │  │
│  │              │───▶│  01 → 02 → 03 → 04 → 05 → 06            │  │
│  │  stack.md    │    │                                          │  │
│  │  decisions   │    │  Each phase has:                         │  │
│  │  glossary    │    │  • Input requirements                    │  │
│  │  spec file   │    │  • Step-by-step instructions             │  │
│  └──────────────┘    │  • Agent persona (optional)              │  │
│                      │  • Definition of Done gate               │  │
│  ┌──────────────┐    └──────────────────────────────────────────┘  │
│  │   RUNNERS    │                        │                          │
│  │              │◀───────────────────────┘                         │
│  │  claude-code │    Thin adapter — invocation only                │
│  │  copilot     │    All logic stays in prompts/                   │
│  └──────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

### Full Pipeline Flow

```
  INPUT: Feature request / problem statement
           │
           ▼
╔══════════════════════════════════╗
║  PHASE 01 — REQUIREMENTS         ║
╠══════════════════════════════════╣
║  1. Clarify the request          ║
║  2. Identify user roles          ║
║  3. Write user stories           ║
║  4. Define acceptance criteria   ║
║  5. Document constraints         ║
║  6. List open questions          ║
╠══════════════════════════════════╣
║  Output: specs/<name>.md (Draft) ║
╚══════════════════════════════════╝
           │
           │  GATE: Open questions resolved? ACs testable?
           ▼
╔══════════════════════════════════╗
║  PHASE 02 — DESIGN               ║  Agent: Architect
╠══════════════════════════════════╣
║  1. Read arch + context files    ║
║  2. Identify affected components ║
║  3. Define interface contracts   ║
║  4. Design data model            ║
║  5. Evaluate alternatives        ║
║  6. Write ADRs if needed         ║
╠══════════════════════════════════╣
║  Output: spec updated, new ADRs  ║
╚══════════════════════════════════╝
           │
           │  GATE: Design accepted? No structural ambiguity?
           ▼
╔══════════════════════════════════╗
║  PHASE 03 — IMPLEMENTATION       ║  Agent: Developer
╠══════════════════════════════════╣
║  1. Read spec + existing code    ║
║  2. Find smallest change needed  ║
║  3. Write production code only   ║
║  4. Self-review against ACs      ║
║  5. Record out-of-scope findings ║
╠══════════════════════════════════╣
║  Output: production code         ║
║          (NO tests written here) ║
╚══════════════════════════════════╝
           │
           │  GATE: All ACs satisfiable? No security issues?
           ▼
╔══════════════════════════════════╗
║  PHASE 04 — TESTS                ║  Agent: Developer
╠══════════════════════════════════╣
║  1. Map each AC to a test case   ║
║  2. Choose unit/integration/e2e  ║
║  3. Write regression tests       ║
║  4. Run full suite               ║
║  5. Report coverage              ║
╠══════════════════════════════════╣
║  Output: test files, suite green ║
║          (NO production changes) ║
╚══════════════════════════════════╝
           │
           │  GATE: All tests pass? No existing regressions?
           ▼
╔══════════════════════════════════╗
║  PHASE 05 — REVIEW               ║  Agent: Reviewer
╠══════════════════════════════════╣
║  1. Verify each AC: ✓ / ~ / ✗   ║
║  2. Audit code quality           ║
║  3. Security review (OWASP)      ║
║  4. Evaluate test coverage       ║
║  5. Write structured report      ║
╠══════════════════════════════════╣
║  Output: review report           ║
║          Approved / Changes Req. ║
╚══════════════════════════════════╝
           │                  │
       Approved           Blocking issues
           │                  │
           │                  └──▶ Back to Phase 03 or 04
           ▼                       (fix → re-test → re-review)
╔══════════════════════════════════╗
║  PHASE 06 — DOCS                 ║
╠══════════════════════════════════╣
║  1. Identify documentation scope ║
║  2. Write inline docstrings      ║
║  3. Update architecture.md       ║
║  4. Update changelog             ║
║  5. Update README if needed      ║
║  6. Close spec (status: Done)    ║
╠══════════════════════════════════╣
║  Output: docs updated            ║
║          spec status: Done       ║
╚══════════════════════════════════╝
           │
           ▼
  DONE — ready for PR / merge
```

### What the AI Reads and When

```
  context/stack.md ──────────────────────────▶ Every phase
  context/decisions.md ──────────────────────▶ Phase 02 (must respect ADRs)
                        ◀────────────────────── Phase 02 (new ADRs written here)
                                               Phase 05 (review checks consistency)
  context/glossary.md ───────────────────────▶ Every phase
  specs/<name>.md ────────────────────────────▶ Every phase (source of truth)
                   ◀──────────────────────────── Phases 01, 02, 05, 06 (updated)
  specs/architecture.md ─────────────────────▶ Phase 02 (design must fit arch)
                         ◀─────────────────────  Phase 06 (updated if arch changed)
```

### Workflow Variations

```
  NEW FEATURE          BUG FIX                    RELEASE
  ───────────          ───────                    ───────
  01 Requirements  ──▶ 01 Root cause analysis ──▶ Validate (tests + lint)
  02 Design            02 Design*                  Document (changelog)
  03 Implementation    03 Targeted fix              Tag
  04 Tests             04 Regression test           Deploy
  05 Review            05 Review                    Verify
  06 Docs              06 Docs*

                            * optional — only if
                              structural changes needed
```

### Spec Lifecycle

```
  [Draft] ──▶ [In Review] ──▶ [Approved] ──▶ [Done]
   Ph.01         Ph.02          Ph.05          Ph.06

  If Ph.05 finds blockers: stays [In Review] until resolved and re-reviewed.
```

### Runner Layer

The runner files add nothing to pipeline logic. They answer one question only: _how do I invoke this phase with tool X?_

```
  runners/claude-code.md     runners/copilot.md
  ──────────────────────     ──────────────────
  Session startup            Copilot Chat panel
  Phase prompt format        @workspace + #file: syntax
  Autonomous multi-phase     Inline chat for Phase 03
  Shell access notes         Manual phase advancement
```

---

## Contributing

Prompts live in `prompts/`. Keep them tool-agnostic — no tool-specific slash commands or syntax. Runner-specific instructions belong exclusively in `runners/`.
