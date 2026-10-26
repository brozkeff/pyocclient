# AGENTS.md

## Project

- This repository is an unofficial maintenance fork of upstream `pyocclient`
  0.6.
- Preserve the public distribution name `pyocclient` and import package
  `owncloud`.
- Keep `source/upstream/` as provenance for the unmodified official source.

## Packaging

- Use `uv` for build and local verification commands.
- Keep packaging PEP 517-compatible through `pyproject.toml`.
- Use PEP 440 local versions based on `0.6`, for example
  `0.6+brozkeff.20260622.sha.a33ddcbb.r1`.
- Do not introduce new runtime dependencies unless required for a documented
  compatibility fix.

## Maintenance

- Prefer minimal compatibility patches over feature work.
- Preserve existing runtime behavior and public APIs unless a bug document or
  ADR explicitly justifies a change.
- Add or update files under `docs/bugs/` for reproducible compatibility issues.
- Record durable architectural decisions under `docs/decisions/`.

## Python

- Target Python 3.10+ for this fork.
- Keep type and syntax choices compatible with the declared Python range.

