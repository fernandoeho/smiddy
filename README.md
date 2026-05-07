# Smiddy

**Tool-agnostic SDLC autonomous pipeline framework.**

Smiddy provides a structured, phase-driven pipeline for software development that runs on any AI coding assistant. All prompts are tool-agnostic — only the adapter layer changes when you switch tools.

---

## Installation

Clone the repository, then run `install.sh` pointing at your project root:

```bash
git clone https://github.com/your-org/smiddy.git
cd smiddy
./install.sh /path/to/your-project
```

| Flag | Description |
|---|---|
| `--claude` | Install only the Claude Code adapter (`.claude/CLAUDE.md`) |
| `--copilot` | Install only the GitHub Copilot adapter (`.copilot/instructions.md`) |
| `--all` | Install both adapters (default) |
| `--force` | Overwrite existing files |

Existing files are skipped by default. Use `--force` to overwrite.

---

## Quick Start

1. **Fill in context** — edit `.smiddy/context/product.md` and `.smiddy/context/stack.md`. Architectural decisions live as individual files in `.smiddy/governance/decisions/`.
2. **Discover existing context** *(existing projects only)* — run `.smiddy/prompts/setup/stack-discovery.md` to auto-fill `stack.md`, then `.smiddy/prompts/setup/architecture-discovery.md` to auto-fill `architecture.md`. For new projects, skip this — the Architect agent (Phase 02) will create `architecture.md`.
3. **Write a spec** — give your raw requirement to the Product Owner agent (Phase 01); it will ask clarifying questions and generate `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md` and a `.pipeline-state.yml` alongside it.
4. **Read the invocation guide** — open `.smiddy/docs/claude-code.md` or `.smiddy/docs/copilot.md` for step-by-step instructions and examples.
5. **Run the pipeline** — follow the phase sequence, feeding each phase prompt to your chosen AI tool.
6. **Resume if interrupted** — if a session ends before a phase completes, run `.smiddy/prompts/setup/resume.md` to pick up where you left off.

---

## Pipeline Phases

| Phase | Prompt | Output |
|---|---|---|
| 01 Requirements | `.smiddy/prompts/phases/01-requirements.md` | Acceptance criteria, constraints — driven by the Product Owner agent |
| 02 Design | `.smiddy/prompts/phases/02-design.md` | Architecture decisions, interfaces — driven by the Architect agent |
| 03 Build | `.smiddy/prompts/phases/03-build.md` | Production code and tests — driven by the Developer agent |
| 04 Review | `.smiddy/prompts/phases/04-review.md` | Review report — driven by the Reviewer agent |
| 05 Docs | `.smiddy/prompts/phases/05-docs.md` | Documentation |

Phases are sequential. Each phase begins with a **gate check** — a quality checklist that must pass before work starts. A failing gate blocks the phase and reports exactly what is missing. Gates are defined in `.smiddy/governance/gates/`.

Phase 01 creates a `.pipeline-state.yml` alongside the spec. Every subsequent phase updates it on entry, gate result, and completion. If a session ends mid-phase, use `.smiddy/prompts/setup/resume.md` to re-enter the pipeline at the correct point without losing progress.

---

## Tool Selection

| Criterion | Claude Code | GitHub Copilot |
|---|---|---|
| Primary interface | Terminal / CLI | VS Code / IDE |
| Best for | Autonomous multi-step tasks | In-editor assistance |
| Tool use / shell access | Native | Extension-dependent |

You can use both simultaneously — Claude Code for pipeline orchestration, Copilot for in-editor autocomplete.

---

## Governance

The `.smiddy/governance/` folder holds all control and oversight artifacts:

| Folder | Purpose |
|---|---|
| `governance/decisions/` | Architectural Decision Records (ADRs). Each decision is a Markdown file; `index.yml` is the searchable index used by phase prompts to find relevant decisions. |
| `governance/standards/` | Coding and design standards discovered or written during the pipeline. `index.yml` lists them by category; standard files are written in Phase 05. |
| `governance/gates/` | Phase transition checklists. Each file defines the quality bar that must pass before the next phase can begin. |

---

## Token Usage Baseline

Smiddy includes an optional Python utility to estimate the token footprint of Smiddy-controlled artifacts.

Run:

```bash
python .smiddy/tools/token_report.py
```

This generates:
```
.smiddy/reports/token-usage.md
.smiddy/reports/token-usage.json
```

The report groups estimated token usage by context, governance, prompts, specs, docs, and other Smiddy artifacts.

This is useful before implementing compression or context optimization.

> **Note:** This is estimated usage, not exact provider billing.
---

## Contributing

Prompts live in `.smiddy/prompts/`. Keep them tool-agnostic — no tool-specific syntax. Tool-specific invocation guides belong in `.smiddy/docs/`; adapter behavior files belong in `.claude/CLAUDE.md` or `.copilot/instructions.md`.
