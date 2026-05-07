#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime, timezone
import re
import json

SUPPORTED_EXTENSIONS = {
    ".md",
    ".mdx",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
}

def scan_files(smiddy_root: Path) -> list[Path]:
    files =[]
    for file_path in smiddy_root.rglob("*"):
        if not file_path.is_file():
            continue

        if file_path.suffix not in SUPPORTED_EXTENSIONS:
            continue

        if should_skip(file_path, smiddy_root):
            continue

        files.append(file_path)

    return files

def should_skip(file_path: Path, smiddy_root: Path) -> bool:
    #Skip files in .smiddy/tools/reports to avoid noise in the report
    relative_path = file_path.relative_to(smiddy_root.parent)
    if str(relative_path).startswith("tools/"):
        return True
    
    return False

def read_file(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")

def count_words(text: str) -> int:
    if not text.strip():
        return 0
    
    return len(re.findall(r"\S+", text))

def estimate_tokens(text: str) -> int:
    # Simple estimation: 1 token ~ 4 characters
    if not text.strip():
        return 0
    
    characters_estimate = (len(text) + 3) // 4
    words_estimate = int(count_words(text) * 1.5 + 0.999)  # Adjusted word count to token estimate
    return max(characters_estimate, words_estimate)

def classify_file(relative_path: str) -> str:
    if relative_path.startswith(".smiddy/context/"):
        return "context"
    
    if relative_path.startswith(".smiddy/governance/gates/"):
        return "governance-gates"
    
    if relative_path.startswith(".smiddy/governance/standards/"):
        return "governance-standards"
    
    if relative_path.startswith(".smiddy/governance/decisions/"):
        return "governance-decisions"
    
    if relative_path.startswith(".smiddy/governance/"):
        return "governance-other"
    
    if relative_path.startswith(".smiddy/prompts/phases/"):
        return "phase-prompts"

    if relative_path.startswith(".smiddy/prompts/setup/"):
        return "setup-prompts"

    if relative_path.startswith(".smiddy/prompts/"):
        return "prompts-other"

    if relative_path.startswith(".smiddy/specs/"):
        return "specs"

    if relative_path.startswith(".smiddy/docs/"):
        return "docs"
    
    return "other"

def analyze_file(file_path: Path, project_root: Path) -> dict:
    content = read_file(file_path)
    relative_path = str(file_path.relative_to(project_root)).replace("\\", "/")

    return {
        "path": relative_path,
        "category": classify_file(relative_path),
        "characters": len(content),
        "words": count_words(content),
        "estimated_tokens": estimate_tokens(content),
    }

def aggregate_by_category(file_stats: list[dict]) -> dict:
    categories = {}

    for file in file_stats:
        category = file["category"]

        if category not in categories:
            categories[category] = {
                "files": 0,
                "characters": 0,
                "words": 0,
                "estimated_tokens": 0,
            }

        categories[category]["files"] += 1
        categories[category]["characters"] += file["characters"]
        categories[category]["words"] += file["words"]
        categories[category]["estimated_tokens"] += file["estimated_tokens"]

    return categories

def format_number(value: int) -> str:
    return f"{value:,}"

def generate_markdown_report(file_stats: list[dict], categories: dict) -> str:
    generated_at = datetime.now(timezone.utc).isoformat()
    total_files = len(file_stats)
    total_characters = sum(file["characters"] for file in file_stats)
    total_words = sum(file["words"] for file in file_stats)
    total_tokens = sum(file["estimated_tokens"] for file in file_stats)
    
    sorted_categories = sorted(
        categories.items(),
        key=lambda item: item[1]["estimated_tokens"],
        reverse=True,
    )

    largest_files = sorted(
        file_stats,
        key=lambda file: file["estimated_tokens"],
        reverse=True,
    )[:20]

    lines = []

    lines.append("# Smiddy Token Usage Report")
    lines.append("")
    lines.append(f"Generated at: `{generated_at}`")
    lines.append("")
    lines.append("Estimator: `generic-char-word-v1`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    lines.append(f"| Files scanned | {format_number(total_files)} |")
    lines.append(f"| Characters | {format_number(total_characters)} |")
    lines.append(f"| Words | {format_number(total_words)} |")
    lines.append(f"| Estimated tokens | {format_number(total_tokens)} |")
    lines.append("")
    lines.append("## Usage by Category")
    lines.append("")
    lines.append("| Category | Files | Estimated Tokens | Share |")
    lines.append("|---|---:|---:|---:|")

    for category, stats in sorted_categories:
        share = 0

        if total_tokens > 0:
            share = stats["estimated_tokens"] / total_tokens * 100

        lines.append(
            f"| {category} | "
            f"{format_number(stats['files'])} | "
            f"{format_number(stats['estimated_tokens'])} | "
            f"{share:.2f}% |"
        )

    lines.append("")
    lines.append("## Largest Files")
    lines.append("")
    lines.append("| File | Category | Estimated Tokens |")
    lines.append("|---|---|---:|")

    for file in largest_files:
        lines.append(
            f"| `{file['path']}` | "
            f"{file['category']} | "
            f"{format_number(file['estimated_tokens'])} |"
        )

    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- This report estimates Smiddy-controlled token usage.")
    lines.append("- This is not exact provider billing.")
    lines.append("- Different AI models tokenize text differently.")
    lines.append("- Use this report as a baseline before token optimization.")

    return "\n".join(lines)

def generate_json_report(file_stats: list[dict], categories: dict) -> dict:
    total_tokens = sum(file["estimated_tokens"] for file in file_stats)

    category_list = []

    for category, stats in categories.items():
        share = 0

        if total_tokens > 0:
            share = stats["estimated_tokens"] / total_tokens * 100

        category_list.append({
            "category": category,
            "files": stats["files"],
            "characters": stats["characters"],
            "words": stats["words"],
            "estimated_tokens": stats["estimated_tokens"],
            "share_percent": round(share, 2),
        })

    category_list = sorted(
        category_list,
        key=lambda item: item["estimated_tokens"],
        reverse=True,
    )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "estimator": "generic-char-word-v1",
        "summary": {
            "files": len(file_stats),
            "characters": sum(file["characters"] for file in file_stats),
            "words": sum(file["words"] for file in file_stats),
            "estimated_tokens": total_tokens,
        },
        "categories": category_list,
        "files": sorted(
            file_stats,
            key=lambda file: file["estimated_tokens"],
            reverse=True,
        ),
    }

def main():
    project_root = Path(__file__).parent.parent.parent
    smiddy_root = project_root / ".smiddy"

    print("Smiddy Token Usage Report")
    print("=========================")

    if not smiddy_root.exists():
        print("Error: .smiddy directory not found. Please run 'smiddy init' first.")
        return
    
    files = scan_files(smiddy_root)
    file_stats = [analyze_file(file_path, project_root) for file_path in files]
    categories = aggregate_by_category(file_stats)

    markdown_report = generate_markdown_report(file_stats, categories)
    json_report = generate_json_report(file_stats, categories)

    reports_dir = smiddy_root / "tools/tokens/reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    markdown_path = reports_dir / "token-usage.md"
    markdown_path.write_text(markdown_report, encoding="utf-8")

    json_path = reports_dir / "token-usage.json"
    json_path.write_text(json.dumps(json_report, indent=2), encoding="utf-8")

    total_tokens = sum(file["estimated_tokens"] for file in file_stats)

    print(f"Files scanned: {format_number(len(file_stats))}")
    print(f"Total estimated tokens: {format_number(total_tokens)}")
    print(f"Wrote report: {markdown_path}")
    print(f"Wrote JSON report: {json_path}")

if __name__ == "__main__":
    main()