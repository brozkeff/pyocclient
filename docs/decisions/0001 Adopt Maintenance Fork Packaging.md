---
status: "Accepted"
date: 2026-06-22
---

# Adopt Maintenance Fork Packaging

## Context and Problem Statement

The official `pyocclient` 0.6 package is the latest upstream release, but it
uses legacy `setup.py` packaging that modern `pip` warns will stop working.
The package is still needed as a Git-installable dependency, with fixes that
remain clearly tied to the last official 0.6 release.

## Decision Drivers

- Keep existing consumers compatible with `import owncloud`.
- Make installation work with current `pip` and `uv`.
- Preserve upstream provenance for auditability.
- Avoid creating a new feature branch disguised as an upstream release.

## Considered Options

- Keep upstream layout and only patch `setup.py`.
- Create a new package name for the fork.
- Promote upstream 0.6 source to repository root and add PEP 517 metadata.

## Decision Outcome

Chosen option: "Promote upstream 0.6 source to repository root and add PEP 517
metadata", because Git installers expect a buildable project at the repository
root and PEP 517 metadata resolves the legacy wheel-build warning.

The fork keeps distribution name `pyocclient` and import package `owncloud`.
Fork builds use PEP 440 local versions based on upstream `0.6`, such as
`0.6+brozkeff.20260622.sha.a33ddcbb.r1`.

### Consequences

- [+] `uv` and modern `pip` can install directly from the GitHub repository.
- [+] Existing code using `import owncloud` does not need changes.
- [+] The local version string clearly marks the build as an NMU-style fork of
  upstream 0.6.
- [-] The fork version is not suitable for upload over upstream `pyocclient`
  on PyPI.

### Confirmation

Confirm by building the package with PEP 517, installing it locally, checking
that `import owncloud` succeeds, and verifying the installed distribution
version starts with `0.6+brozkeff`.

## More Information

The unmodified upstream source is retained under `source/upstream/`. Bug notes
for the initial maintenance work are recorded under `docs/bugs/`.

