# Standards

Coding standards live as individual files in `.smiddy/standards/<category>/`. Use `.smiddy/standards/index.yml` to find standards by category without loading every file.

The AI agent reads `index.yml` before Phase 02 (Design) and Phase 03 (Build) to identify which standard files are relevant to the current work.

---

## How to Add a Standard

Standards are created in two ways:

1. **Setup** — run `.smiddy/prompts/setup/standards-discovery.md` to extract patterns from your existing codebase
2. **Automatically** — Phase 05 (Documentation) writes new standards flagged by the Reviewer in Phase 04

To add one manually:

1. Choose or create a category folder: `api/`, `database/`, `testing/`, `error-handling/`, `frontend/`, `validation/`, `logging/`, or any other area
2. Create `.smiddy/standards/<category>/<standard-name>.md` using the format below
3. Add an entry to `.smiddy/standards/index.yml`

When a standard is retired, do not delete the file — add `retired: true` to its index entry and leave the file in place.

---

## Standard File Format

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

[One short paragraph explaining the rationale. This is what turns a rule into a decision a future agent can reason about.]

## Exceptions

[When this pattern does not apply. If none, write: "None — apply in all cases."]
```

---

## Writing Guidelines

Standards are read by AI agents during Phases 02 and 03. Every word costs tokens. Write for scannability, not completeness.

- **Lead with the rule.** Each bullet should state what to do before explaining why.
- **Code examples over prose.** Show the pattern; don't describe it.
- **One concept per file.** Do not combine unrelated patterns.
- **Short Why sections.** One paragraph maximum.

---

## Example

See `api/response-envelope.md` for a worked example of the format.
