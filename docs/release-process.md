# Release Process

This document describes how releases are created for MQ Trace Lite.

---

## Overview

Releases are fully automated using GitHub Actions.

No manual release creation is required.

---

## Versioning

We follow semantic versioning:

vMAJOR.MINOR.PATCH

Example: v0.1.0

---

## How to Create a Release

### 1. Ensure main branch is stable

- All tests must pass
- CI must be green

---

### 2. Create a Git tag

```bash
git tag v0.1.0
git push origin v0.1.0
```

---

## What Happens Automatically

When a tag is pushed:

1. GitHub Actions triggers the release workflow
2. Tests are executed
3. Python package is built using Poetry
4. A GitHub Release is created
5. Build artifacts are attached:
    - .whl
    - .tar.gz

---

## Artifacts

The following files are included in each release:

- Wheel package (.whl)
- Source distribution (.tar.gz)

---

## Notes
- Releases are immutable once created
- Do not reuse tags
- Always increment version numbers

---

## Future
- Publish to TestPyPI
- Publish to PyPI using Trusted Publishing