# Setup Guide

## Requirements

- Python 3.11+
- Poetry

---

## Install Poetry

If not installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

---

## Verify Installation

```bash
poetry --version
```

---

## Install Project Dependencies

From project root:

```bash
poetry install
```

---

## Run CLI

```bash
poetry run python -m mqtrace.cli.main --help
```

---

## Example

```bash
poetry run python -m mqtrace.cli.main inspect --queue DLQ.TEST
```

---

## Notes

* --no-root is used because the project is not packaged yet
* This will change in future steps