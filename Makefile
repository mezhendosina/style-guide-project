.PHONY: install serve build lint check

install:
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r requirements.txt

serve:
	.venv/bin/mkdocs serve

build:
	.venv/bin/mkdocs build --strict

lint:
	npx --yes markdownlint-cli2@0.23.3

check:
	python3 scripts/check_docs.py

