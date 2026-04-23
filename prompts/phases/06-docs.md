# Phase 06 — Documentation

**Input:** Approved implementation (Phase 05 review: Approved). Spec at `.smiddy/specs/<feature-name>.md`.
**Output:** Updated documentation. Spec status set to Done.

**Requires:**
- `.smiddy/specs/architecture.md` — to update if structure changed

---

## Instructions

Your job is to produce documentation that makes the shipped feature understandable and maintainable. Write for the next developer, not for the current one.

### Step 1 — Identify documentation targets

Review what changed. For each affected area, determine whether documentation needs to be created or updated:

| Area | Update if... |
|---|---|
| Public API | New endpoints, changed signatures, new error codes |
| Configuration | New environment variables, flags, or config keys |
| Data model | New tables, fields, or schema changes |
| Architecture | New components, changed data flows, new external dependencies |
| Runbook / ops | Deployment steps, rollback procedure, new operational concerns |
| User-facing | Changes to UI, commands, or behavior visible to end users |
| Changelog | Any user-visible change |

### Step 2 — Write inline documentation

For every new public function, class, or module:
- Write a docstring that explains *what it does* and *when to use it*
- Document non-obvious parameters and return values
- Note side effects, preconditions, or invariants that a caller must know

Do not document what the code obviously does. Document the why, the contract, and the gotchas.

### Step 3 — Update architecture documentation

If Phase 02 introduced new components, changed data flows, or added external dependencies:
- Update `.smiddy/specs/architecture.md` to reflect the current state
- Do not leave architecture docs describing a state that no longer exists

### Step 4 — Update the changelog

Add an entry to the project changelog (if one exists) following the project's existing format. Include:
- The user-visible change in plain language
- Any migration steps required by existing users

### Step 5 — Update the README (if applicable)

If the feature changes how developers set up, run, or configure the project:
- Update the relevant README section
- Verify that the setup instructions still work end-to-end

### Step 6 — Close the spec

Update `.smiddy/specs/<feature-name>.md`:
- Set status to **Done**
- Fill in "Last updated" date
- Confirm the "Definition of Done" checklist is complete

---

## Definition of Done for This Phase

- [ ] Inline documentation written for all new public interfaces
- [ ] Architecture docs updated if structure changed
- [ ] Changelog entry added for all user-visible changes
- [ ] README updated if setup or usage changed
- [ ] Spec status set to Done
- [ ] No documentation describes a state that no longer exists
