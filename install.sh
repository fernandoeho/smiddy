#!/usr/bin/env bash
set -euo pipefail

SMIDDY_ROOT="$(cd "$(dirname "$0")" && pwd)"

# ── defaults ──────────────────────────────────────────────────────────────────
TARGET_DIR="$PWD"
INSTALL_CLAUDE=false
INSTALL_COPILOT=false
FORCE=false

# ── helpers ───────────────────────────────────────────────────────────────────
usage() {
  cat <<EOF
Usage: install.sh [TARGET_DIR] [OPTIONS]

Installs the Smiddy pipeline framework into a project directory.

Arguments:
  TARGET_DIR        Destination project root (default: current directory)

Options:
  --claude          Install Claude Code adapter only (.claude/CLAUDE.md)
  --copilot         Install GitHub Copilot adapter only (.copilot/instructions.md)
  --all             Install both adapters (default when neither flag is given)
  --force           Overwrite existing files
  -h, --help        Show this help message

Examples:
  install.sh                        # install into current directory (both adapters)
  install.sh ~/projects/myapp       # install into a specific directory
  install.sh ~/projects/myapp --claude --force
EOF
}

log()  { printf '  \033[32m✓\033[0m %s\n' "$1"; }
warn() { printf '  \033[33m~\033[0m %s (skipped — use --force to overwrite)\n' "$1"; }
err()  { printf '  \033[31m✗\033[0m %s\n' "$1" >&2; }

copy_file() {
  local src="$1"
  local dest="$2"

  if [[ -e "$dest" ]] && [[ "$FORCE" == false ]]; then
    warn "$dest"
    return
  fi

  mkdir -p "$(dirname "$dest")"
  cp "$src" "$dest"
  log "$dest"
}

copy_dir() {
  local src_dir="$1"   # relative to SMIDDY_ROOT
  local dest_dir="$2"  # absolute destination

  while IFS= read -r -d '' src_file; do
    local relative="${src_file#"$SMIDDY_ROOT/$src_dir/"}"
    copy_file "$src_file" "$dest_dir/$src_dir/$relative"
  done < <(find "$SMIDDY_ROOT/$src_dir" -type f -print0)
}

# ── argument parsing ──────────────────────────────────────────────────────────
for arg in "$@"; do
  case "$arg" in
    --claude)  INSTALL_CLAUDE=true ;;
    --copilot) INSTALL_COPILOT=true ;;
    --all)     INSTALL_CLAUDE=true; INSTALL_COPILOT=true ;;
    --force)   FORCE=true ;;
    -h|--help) usage; exit 0 ;;
    -*) err "Unknown option: $arg"; usage; exit 1 ;;
    *)  TARGET_DIR="$arg" ;;
  esac
done

# default: install both adapters if neither flag was specified
if [[ "$INSTALL_CLAUDE" == false && "$INSTALL_COPILOT" == false ]]; then
  INSTALL_CLAUDE=true
  INSTALL_COPILOT=true
fi

TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd)" || {
  err "Target directory does not exist: $TARGET_DIR"
  exit 1
}

# ── main ──────────────────────────────────────────────────────────────────────
echo
echo "Installing Smiddy into: $TARGET_DIR"
echo

echo "── Pipeline files ───────────────────────────────────────────"
for dir in context specs prompts workflows runners; do
  copy_dir "$dir" "$TARGET_DIR"
done

if [[ "$INSTALL_CLAUDE" == true ]]; then
  echo
  echo "── Claude Code adapter ──────────────────────────────────────"
  copy_file "$SMIDDY_ROOT/.claude/CLAUDE.md" "$TARGET_DIR/.claude/CLAUDE.md"
fi

if [[ "$INSTALL_COPILOT" == true ]]; then
  echo
  echo "── GitHub Copilot adapter ───────────────────────────────────"
  copy_file "$SMIDDY_ROOT/.copilot/instructions.md" "$TARGET_DIR/.copilot/instructions.md"
fi

echo
echo "Done. Next steps:"
echo "  1. Edit context/stack.md with your project's tech stack."
echo "  2. Edit context/decisions.md with any standing architectural decisions."
echo "  3. Copy specs/_template.md to specs/<feature>.md and fill it in."
echo "  4. Pick a workflow from workflows/ and follow the phase sequence."
echo
