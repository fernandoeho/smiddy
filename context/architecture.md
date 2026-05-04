# System Architecture

<!--
  New project: leave this file blank. The Architect agent (Phase 02) will populate it.
  Existing project: run .smiddy/prompts/setup/architecture-discovery.md before Phase 02,
  or fill it in manually. The AI reads this file to understand the current system shape
  before designing new features.
  Living document: update via Phase 05 whenever structure changes.
-->

**Status:** Living document — update when significant structural decisions are made.
**Last updated:** [YYYY-MM-DD]

---

## Overview

_One paragraph describing the system's purpose, primary actors, and high-level boundaries._

---

## Architecture Style

_e.g., Monolith, Modular Monolith, Microservices, Event-driven, Serverless._

Rationale: _why this style was chosen over alternatives._

---

## System Context

```
[External Actor] --> [This System] --> [External Dependency]
```

_Replace with an actual diagram or ASCII sketch. Describe each external interaction._

---

## Component Map

| Component | Responsibility | Owner team |
|---|---|---|
| | | |

---

## Key Data Flows

### Flow 1: [Name]

```
[Component A] --(event/call)--> [Component B] --(event/call)--> [Component C]
```

_Describe the trigger, steps, and terminal state._

---

## Persistence

| Store | Technology | Data it holds |
|---|---|---|
| | | |

---

## Authentication & Authorization

_Describe the auth model: who authenticates, how sessions/tokens work, what the permission model looks like._

---

## Cross-Cutting Concerns

- **Logging:** _format, levels, storage_
- **Error handling:** _strategy, error taxonomy_
- **Feature flags:** _tool, rollout strategy_
- **Rate limiting:** _where enforced, thresholds_

---

## Known Constraints

_Limitations imposed by platform, compliance, or existing systems that shape design choices._

---

## Significant Decisions

_See `.smiddy/governance/decisions/index.yml` for the full ADR index. Key decisions summarized here:_

| Decision | Rationale |
|---|---|
| | |
