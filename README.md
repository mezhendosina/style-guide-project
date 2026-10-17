# API Writing Guide

Практическое руководство по стилю русскоязычной документации REST API. Проект выполнен по методологии Docs as Code: правила хранятся в Markdown, проверяются автоматически и публикуются через MkDocs.

## Что внутри

- конкретные правила языка, структуры, оформления и описания API;
- шаблоны how-to и справочника метода API;
- два документа, написанных по стайл-гайду;
- автоматические проверки Markdown, ссылок, навигации и сборки;
- отчёт, который отвечает на пункты лабораторной работы № 3.

## Локальный запуск

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/mkdocs serve
```

Откройте <http://127.0.0.1:8000/>. Строгая сборка:

```bash
.venv/bin/mkdocs build --strict
```

Быстрая проверка ссылок и навигации не требует сторонних пакетов:

```bash
python3 scripts/check_docs.py
```

Markdown-линтинг:

```bash
npx --yes markdownlint-cli2@0.23.3
```

## Публикация

Workflow `.github/workflows/ci.yml` проверяет каждый Pull Request. После слияния в `main` он публикует сайт в ветку `gh-pages`. В настройках репозитория выберите **Settings → Pages → Deploy from a branch → gh-pages / root**.

## Структура

```text
docs/
├── rules/       # нормативные правила
├── patterns/    # шаблоны и чек-лист
├── examples/    # апробация стайл-гайда
└── project/     # исследование и отчёт
```

Порядок внесения изменений описан в [CONTRIBUTING.md](CONTRIBUTING.md).
