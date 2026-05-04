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

1. **Fill in context** — edit `.smiddy/context/product.md`, `.smiddy/context/stack.md`, and `.smiddy/context/glossary.md`. Architectural decisions live as individual files in `.smiddy/decisions/`.
2. **Discover existing context** *(existing projects only)* — run `.smiddy/prompts/setup/stack-discovery.md` to auto-fill `stack.md`, then `.smiddy/prompts/setup/architecture-discovery.md` to auto-fill `architecture.md`. For new projects, skip this — the Architect agent (Phase 02) will create `architecture.md`.
3. **Write a spec** — give your raw requirement to the Product Owner agent (Phase 01); it will ask clarifying questions and generate `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md` for you.
4. **Read the invocation guide** — open `.smiddy/docs/claude-code.md` or `.smiddy/docs/copilot.md` for step-by-step instructions and examples.
5. **Run the pipeline** — follow the phase sequence, feeding each phase prompt to your chosen AI tool.

---

## Pipeline Phases

| Phase | Prompt | Output |
|---|---|---|
| 01 Requirements | `.smiddy/prompts/phases/01-requirements.md` | Acceptance criteria, constraints — driven by the Product Owner agent |
| 02 Design | `.smiddy/prompts/phases/02-design.md` | Architecture decisions, interfaces — driven by the Architect agent |
| 03 Build | `.smiddy/prompts/phases/03-build.md` | Production code and tests — driven by the Developer agent |
| 04 Review | `.smiddy/prompts/phases/04-review.md` | Review report — driven by the Reviewer agent |
| 05 Docs | `.smiddy/prompts/phases/05-docs.md` | Documentation |

Phases are sequential by default.

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

Prompts live in `.smiddy/prompts/`. Keep them tool-agnostic — no tool-specific syntax. Tool-specific invocation guides belong in `.smiddy/docs/`; adapter behavior files belong in `.claude/CLAUDE.md` or `.copilot/instructions.md`.
