# PDM Crash with python:3.10-slim-bookworm

This repository reproduces a crash issue with PDM when using the `python:3.10-slim-bookworm` Docker image as a base.

## Issue Description

PDM crashes when running `pdm sync` in a `python:3.10-slim-bookworm` container, but works fine with the regular `python:3.10` image.

**Original issue observed in:** https://gitlab.gitguardian.ovh/gg-code/data-engineering/basalt/-/jobs/5465634

## Reproduction

The GitHub Actions workflow in `.github/workflows/test-slim.yml` demonstrates the issue by running the same PDM operations in both environments:

1. **`test-slim-bookworm` job**: Uses `python:3.10-slim-bookworm` - Expected to fail
2. **`test-regular-python` job**: Uses `python:3.10` - Expected to succeed

## Project Structure

```
├── .github/workflows/test-slim.yml  # GitHub Actions workflow
├── pyproject.toml                   # PDM project configuration
├── src/pdm_slim_repro/             # Simple Python package
│   ├── __init__.py
│   └── main.py
└── README.md                        # This file
```

## Local Testing

To test locally with Docker:

### Test with slim-bookworm (should fail):
```bash
docker run --rm -v $(pwd):/app -w /app python:3.10-slim-bookworm bash -c "
  pip install pdm && 
  pdm sync
"
```

### Test with regular python (should work):
```bash
docker run --rm -v $(pwd):/app -w /app python:3.10 bash -c "
  pip install pdm && 
  pdm sync
"
```
