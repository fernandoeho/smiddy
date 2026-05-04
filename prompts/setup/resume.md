# Resume Pipeline

Use this prompt to re-enter a pipeline that was interrupted — by a token reset, session close, or any other break in continuity.

---

## Instructions

### Step 1 — Locate the active spec

If the user provides a spec path, use it directly.

Otherwise, scan `.smiddy/specs/` for folders containing a `.pipeline-state.yml` file where `pipeline.current_phase_name` is not `docs` with status `done`. List any matches and ask the user which one to resume.

### Step 2 — Read the state file

Open `.pipeline-state.yml` in the spec folder. Note:
- `pipeline.current_phase` — the phase number to resume
- `pipeline.current_phase_name` — the phase name
- The `status` of the current phase: `in_progress` or `blocked`

### Step 3 — Re-enter the correct phase

Load the phase prompt at `.smiddy/prompts/phases/0<N>-<phase-name>.md`.

**If status is `in_progress`:**
Re-enter the phase from the beginning. Phases are designed to be idempotent — re-reading context, re-checking completed work, and continuing from where the spec left off is safe. Do not repeat work already reflected in the spec; pick up from the first incomplete step.

**If status is `blocked`:**
Re-run the gate for this phase first. If the gate now passes, update the state file (`status: in_progress`, `gate_passed: true`) and proceed. If the gate still fails, report what remains unresolved and stop.

### Step 4 — Continue normally

Once re-entered, follow the phase prompt as usual. State updates, gate checks, and Definition of Done all apply normally from this point.
