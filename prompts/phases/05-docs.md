# Phase 05 — Documentation

**Input:** Approved implementation (Phase 04 review: Approved). Spec at `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md`.
**Output:** Updated documentation. Spec status set to Done.

**Requires:**
- `.smiddy/context/architecture.md` — to update if structure changed
- `.smiddy/standards/index.yml` — to update if new standards were flagged in Phase 04

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
- Update `.smiddy/context/architecture.md` to reflect the current state
- Do not leave architecture docs describing a state that no longer exists

### Step 4 — Update the changelog

Add an entry to the project changelog (if one exists) following the project's existing format. Include:
- The user-visible change in plain language
- Any migration steps required by existing users

### Step 5 — Update the README (if applicable)

If the feature changes how developers set up, run, or configure the project:
- Update the relevant README section
- Verify that the setup instructions still work end-to-end

### Step 6 — Write flagged standards

Read the "Standards Candidates" section of the Phase 04 review report.

If candidates were listed:

For each candidate, draft a standard file following the format in `prompts/setup/standards-discovery.md` (Name, Pattern, Rules, Why, Exceptions). Use the code introduced in this feature as the code example — it is the authoritative implementation of the pattern.

Write each standard to `.smiddy/standards/<category>/<standard-name>.md` and add an entry to `.smiddy/standards/index.yml`:

```yaml
<category>:
  <standard-name>:
    description: <one-line description>
    file: <category>/<standard-name>.md
```

Keep entries alphabetical within each category.

If the Phase 04 report recorded "None" for Standards Candidates, skip this step.

### Step 7 — Close the spec

Update `.smiddy/specs/<yyyy-mm-dd>-<feature-name>/<yyyy-mm-dd>-<feature-name>.md`:
- Set status to **Done**
- Fill in "Last updated" date
- Confirm the "Definition of Done" checklist is complete

---

## Definition of Done for This Phase

- [ ] Inline documentation written for all new public interfaces
- [ ] Architecture docs updated if structure changed
- [ ] Changelog entry added for all user-visible changes
- [ ] README updated if setup or usage changed
- [ ] Flagged standards written to `.smiddy/standards/` and index updated (or "None" confirmed)
- [ ] Spec status set to Done
- [ ] No documentation describes a state that no longer exists
