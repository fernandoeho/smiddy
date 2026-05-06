# Changelog

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