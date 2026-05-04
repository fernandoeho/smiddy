# Setup: Standards Discovery

**Purpose:** Extract your team's opinionated coding patterns from existing source code into documented, reusable standards.
**When to run:** After `stack-discovery.md` and `architecture-discovery.md`. Run once per focus area; repeat for additional areas as needed.
**Output:** Standard files in `.smiddy/governance/standards/<category>/` and an updated `.smiddy/governance/standards/index.yml`.

> **What this is not:** This prompt does not rediscover the tech stack (tools, versions) or system architecture (components, data flows). It discovers *how* your team writes code within that stack — patterns that a new developer or AI agent would not know without being told.

---

## Instructions

Your job is to read existing source code and surface patterns that are opinionated, tribal, or repeated — then document them as concise standards that future agents can use without re-reading the whole codebase.

### Step 1 — Check existing standards

Read `.smiddy/governance/standards/index.yml` to see what has already been documented. This prevents duplicating standards already captured.

If the file does not exist or is empty, there are no existing standards yet.

### Step 2 — Identify focus areas

Scan the top-level source directories to identify 3–5 candidate focus areas. A focus area should correspond to a part of the codebase with enough code to have consistent patterns.

Examples of useful focus areas:

- **Conventions** — naming, file structure, error handling patterns, commit format. Start here if running standards-discovery for the first time; these are the highest-value standards for a new agent to know.
- **API routes** — how requests are handled, responses structured, errors returned
- **Database** — how queries are written, transactions managed, migrations structured
- **Testing** — how tests are named, structured, what gets mocked vs. faked
- **Error handling** — error classes, codes, propagation strategy
- **Frontend components** — component structure, state management, styling patterns
- **Validation** — where and how input is validated
- **Logging** — what gets logged, at what level, with what context

If `stack-discovery.md` was run first, it may have noted observed conventions as suggested starting areas — use those as candidates.

Present the areas you identified and ask the user to select one to start with.

### Step 3 — Analyse the chosen area

Read 5–10 representative source files from the chosen area. Look specifically for patterns that are:

- **Opinionated** — choices that could have gone differently (e.g. cursor-based pagination instead of offset)
- **Tribal** — things a new contributor would not know without being told (e.g. custom error codes, specific response shapes)
- **Consistent** — patterns repeated across multiple files, not one-offs

Do not surface patterns that are standard framework behavior, widely documented library conventions, or obvious from the tooling.

### Step 4 — Present findings

List 3–6 candidate standards found in the chosen area. For each, provide:

- A short name
- One sentence describing the pattern observed
- 2–3 example files where you found it

Ask the user which to document. They can select all, a subset, or suggest corrections.

### Step 5 — For each selected standard, capture the rationale

Process one standard at a time. Before drafting, ask 1–2 clarifying questions to understand the *why*. For example:

- "What problem does this pattern solve? Why not use [the common alternative]?"
- "Are there situations where this pattern should not be used?"
- "What is the most common mistake a new developer or AI agent makes with this?"

Wait for the user's response before drafting.

### Step 6 — Draft the standard

Using the user's answers, draft the standard following this format exactly:

```markdown
# [Standard Name]

[One-sentence rule — the single most important thing to remember.]

## Pattern

```[language]
[Minimal code example showing the correct pattern. Under 20 lines.]
```

## Rules

- [Bullet points. Lead with the rule, not the reason. One line each.]

## Why

[One short paragraph. Explain the rationale — what this pattern prevents or enables. This is what turns a rule into a decision a future agent can reason about.]

## Exceptions

[When this pattern does not apply. If none, write: "None — apply in all cases."]
```

Show the draft to the user and ask for approval before writing the file.

### Step 7 — Write the file and update the index

Once the user approves, write the standard to `.smiddy/governance/standards/<category>/<standard-name>.md`.

- Use lowercase, hyphenated names for both category and file (e.g. `api/response-envelope.md`, `testing/naming.md`)
- If a related standard file already exists in the category, check whether to append rather than create a new file

Then add an entry to `.smiddy/governance/standards/index.yml`:

```yaml
<category>:
  <standard-name>:
    description: <one-line description matching the standard's opening sentence>
    file: <category>/<standard-name>.md
```

Keep entries alphabetical within each category.

Repeat Steps 5–7 for each remaining selected standard before moving on.

### Step 8 — Offer to continue

After all selected standards are written, summarise what was created and ask whether to discover standards in another area.

---

## Writing guidelines

Standards are read by AI agents during Phases 02 and 03. Every word costs tokens. Write for scannability, not completeness.

- **Lead with the rule.** Each bullet should state what to do before explaining why.
- **Code examples over prose.** Show the pattern; don't describe it.
- **One concept per file.** Do not combine unrelated patterns.
- **Short Why sections.** One paragraph maximum. The goal is to enable judgment, not justify at length.

**Good:**

```markdown
# Error Response Shape

All API errors use `{ success: false, error: { code, message } }`.

## Pattern

```json
{ "success": false, "error": { "code": "AUTH_001", "message": "Token expired." } }
```

## Rules

- Always include both `code` and `message`
- Log the full error server-side; return only the safe message to the client
- Error codes follow the pattern `DOMAIN_NNN` (e.g. `AUTH_001`, `DB_002`)

## Why

Frontend can always check `success` first, then branch on `code` without inspecting message text. Consistent codes make alerting rules and client-side error handling predictable.

## Exceptions

None — apply in all cases.
```

**Bad:**

```markdown
# Error Handling Guidelines

When an error occurs in our application, we have established a consistent pattern for how errors should be formatted and returned to the client. This helps maintain consistency across our API and makes it easier for frontend developers to handle errors appropriately in a uniform way across all endpoints...
```

---

## Definition of Done

- [ ] At least 3 standards written for the chosen area
- [ ] Each standard has a code example, rules list, and a Why section
- [ ] No framework-default or obvious patterns documented — only opinionated, tribal, or non-obvious ones
- [ ] All new standards added to `.smiddy/governance/standards/index.yml`
- [ ] Index entries are alphabetically ordered within each category
