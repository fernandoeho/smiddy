# Changelog

## 0.2.0 - 2026-05-07

### Added

- Introduced **Token Usage Baseline**, a Smiddy-native way to estimate the token footprint of project artifacts before optimization.
- Added `.smiddy/tools/token_report.py`, an optional Python utility that scans Smiddy-controlled markdown and configuration files.
- Added generated Markdown and JSON reports under `.smiddy/reports/`.
- Added token usage breakdowns by artifact category, including context, governance, prompts, specs, docs, and other files.
- Added largest-file reporting to help users identify the main contributors to context size.
- Added support for `--top`, `--no-write`, and `--root` options.
- Added `.smiddy/prompts/setup/token-usage.md` to help AI assistants run and interpret the baseline report.

### Documentation

- Added README documentation for the Token Usage Baseline workflow.
- Added a note clarifying that reported usage is estimated, not exact provider billing.


## v0.1.0 - 2026-05-05

### Added
- Initial public release of Smiddy.
- Tool-agnostic SDLC autonomous pipeline framework.
- Phase-driven workflow: Requirements, Design, Build, Review, and Docs.
- Persona-based execution through Product Owner, Architect, Developer, and Reviewer roles.
- Claude Code adapter.
- GitHub Copilot adapter.
- Governance structure for decisions, standards, and gates.
- Phase gate checks to control quality before execution.
- Pipeline state tracking with `.pipeline-state.yml`.
- Resume prompt for interrupted sessions.
- Installation script for applying Smiddy to existing projects.

### Known Limitations
- Manual prompt-driven execution.
- No package manager distribution yet.
- No automated CLI beyond `install.sh`.
- No release automation yet.
