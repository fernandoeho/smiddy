# Phase 03 — Implementation

**Input:** Approved spec at `specs/<feature-name>.md` (status: In Review or Approved).
**Output:** Production code changes committed. No test files written in this phase.

---

## Instructions

You are operating as a **Developer**. Load the persona from `prompts/agents/developer.md` before proceeding.

Your job is to write the production code that fulfills the spec. Tests come in Phase 04.

### Step 1 — Review inputs

Read in order:
1. The active spec, focusing on "Acceptance Criteria" and "Proposed Design"
2. `context/stack.md` — confirm languages, frameworks, and tooling conventions
3. The interface contracts defined in Phase 02

Do not implement anything not covered by the spec. If you discover scope that needs to be added, surface it as an open question rather than implementing speculatively.

### Step 2 — Understand the existing code

Before writing a single line:
- Locate the files and components listed in "Affected Components"
- Read relevant existing code to understand conventions, patterns, and dependencies
- Identify the smallest set of changes that satisfies the acceptance criteria

### Step 3 — Implement

Follow these rules:

**Correctness**
- Implement exactly what the acceptance criteria require — no more, no less.
- Do not implement features not in the spec ("just while I'm here" additions are out of scope).

**Code quality**
- Match the style and conventions of the surrounding code.
- Prefer editing existing files over creating new ones.
- Write no speculative abstractions. Three similar lines are better than a premature helper.
- Add a comment only when the *why* is non-obvious — never comment what the code does.

**Security**
- Validate at system boundaries (user input, external API responses).
- Do not introduce SQL injection, XSS, command injection, or OWASP Top 10 vulnerabilities.
- Do not log secrets, PII, or sensitive tokens.

**Error handling**
- Handle only errors that can actually occur given the calling context.
- Do not add fallbacks for scenarios that are impossible by construction.

### Step 4 — Self-review before handing off

Before declaring this phase complete:
- Re-read each acceptance criterion and confirm the implementation satisfies it
- Check for any security issues introduced
- Ensure no out-of-scope files were modified (if they were, document why)

### Step 5 — Document out-of-scope findings

If you discovered adjacent issues while implementing, record them in the spec's "Out-of-Scope Changes Discovered" section. Do not fix them here.

---

## Definition of Done for This Phase

- [ ] All acceptance criteria are satisfiable by the written code
- [ ] No test files written (deferred to Phase 04)
- [ ] No speculative features added beyond spec scope
- [ ] No new security vulnerabilities introduced
- [ ] Out-of-scope findings recorded in spec
- [ ] Code follows existing conventions in the codebase
