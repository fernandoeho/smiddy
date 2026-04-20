# Smiddy

**Tool-agnostic SDLC autonomous pipeline framework.**

Smiddy provides a structured, phase-driven pipeline for software development that runs on any AI coding assistant. All prompts and workflows are runtime-neutral — the runner layer is the only thing that changes when you switch tools.

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

1. **Fill in context** — edit `.smiddy/context/stack.md`, `.smiddy/context/decisions.md`, and `.smiddy/context/glossary.md`.
2. **Write a spec** — give your raw requirement to the Product Owner agent (Phase 01); it will ask clarifying questions and generate `.smiddy/specs/<feature-name>.md` for you.
3. **Pick a workflow** — open the relevant file in `.smiddy/workflows/`.
4. **Pick a runner** — open `.smiddy/runners/claude-code.md` or `.smiddy/runners/copilot.md` for invocation instructions.
5. **Run the pipeline** — follow the phase sequence, feeding each phase prompt to your chosen AI tool.

---

## Pipeline Phases

| Phase | Prompt | Output |
|---|---|---|
| 01 Requirements | `.smiddy/prompts/phases/01-requirements.md` | Acceptance criteria, constraints — driven by the Product Owner agent |
| 02 Design | `.smiddy/prompts/phases/02-design.md` | Architecture decisions, interfaces — driven by the Architect agent |
| 03 Implementation | `.smiddy/prompts/phases/03-implementation.md` | Working code — driven by the Developer agent |
| 04 Tests | `.smiddy/prompts/phases/04-tests.md` | Test suite — driven by the Developer agent |
| 05 Review | `.smiddy/prompts/phases/05-review.md` | Review report — driven by the Reviewer agent |
| 06 Docs | `.smiddy/prompts/phases/06-docs.md` | Documentation |

Phases are sequential by default. Workflows may permit skipping phases for specific scenarios (e.g. bug fixes).

---

## Tool Selection

| Criterion | Claude Code | GitHub Copilot |
|---|---|---|
| Primary interface | Terminal / CLI | VS Code / IDE |
| Best for | Autonomous multi-step tasks | In-editor assistance |
| Tool use / shell access | Native | Extension-dependent |

You can use both simultaneously — Claude Code for pipeline orchestration, Copilot for in-editor autocomplete.

---

## Contributing

Prompts live in `.smiddy/prompts/`. Keep them tool-agnostic — no tool-specific syntax. Runner-specific instructions belong exclusively in `.smiddy/runners/`.
