# Token Usage Baseline

Use this prompt to measure the current token footprint of this Smiddy project before making token-efficiency, compression, context-loading, or prompt optimization changes.

## Objective

Generate a baseline report showing estimated token usage across Smiddy-controlled artifacts.

## Instructions

1. Run the token report utility from the project root:

```bash
python .smiddy/tools/tokens/token_report.py