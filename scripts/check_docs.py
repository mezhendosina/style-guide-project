#!/usr/bin/env python3
"""Проверяет навигацию MkDocs, локальные ссылки и базовую структуру страниц."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONFIG = ROOT / "mkdocs.yml"
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
NAV_PAGE = re.compile(r"^\s+-\s+[^:]+:\s+([^#][^\s]*\.md)\s*$", re.MULTILINE)
FENCED_BLOCK = re.compile(r"(?ms)^(`{3,}|~{3,}).*?^\1\s*$")


def markdown_files() -> list[Path]:
    return sorted(DOCS.rglob("*.md"))


def content_files() -> list[Path]:
    root_pages = [ROOT / name for name in ("README.md", "CONTRIBUTING.md", "SUBMISSION.md")]
    return root_pages + markdown_files()


def check_page_shape(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    prose = FENCED_BLOCK.sub("", text)
    headings = re.findall(r"(?m)^# (.+)$", prose)
    if len(headings) != 1:
        errors.append(f"{path.relative_to(ROOT)}: ожидается один H1, найдено {len(headings)}")
    if "\t" in text:
        errors.append(f"{path.relative_to(ROOT)}: найден символ табуляции")


def check_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith(("#", "mailto:")):
            continue
        relative = unquote(parsed.path)
        if not relative:
            continue
        resolved = (path.parent / relative).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: ссылка выходит за пределы проекта: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: не найдена цель ссылки: {target}")


def check_navigation(errors: list[str]) -> None:
    config = CONFIG.read_text(encoding="utf-8")
    listed = {match.group(1) for match in NAV_PAGE.finditer(config)}
    existing = {str(path.relative_to(DOCS)) for path in markdown_files()}
    missing = listed - existing
    orphaned = existing - listed
    for item in sorted(missing):
        errors.append(f"mkdocs.yml: страница навигации не существует: {item}")
    for item in sorted(orphaned):
        errors.append(f"mkdocs.yml: страница не добавлена в навигацию: {item}")


def main() -> int:
    errors: list[str] = []
    for path in content_files():
        check_page_shape(path, errors)
        check_links(path, errors)
    check_navigation(errors)
    if errors:
        print("Проверка документации завершилась с ошибками:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: проверено Markdown-файлов — {len(content_files())}; ссылки и навигация корректны.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
