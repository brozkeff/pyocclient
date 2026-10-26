# pyocclient 0.6 Brozkeff maintenance fork

This is an unofficial maintenance fork of `pyocclient` 0.6, the Python
client library for ownCloud. The distribution name remains `pyocclient` and
the import package remains `owncloud`.

The fork starts from the last official 0.6 source release and applies small
compatibility fixes for current Python packaging tools and Python 3 runtimes.
It is intended for direct installation from Git rather than publication to
PyPI.

## Install

With `uv`:

```bash
uv add "pyocclient @ git+https://github.com/brozkeff/pyocclient.git"
```

With `pip`:

```bash
pip install "pyocclient @ git+https://github.com/brozkeff/pyocclient.git"
```

To pin a specific fork release tag:

```bash
uv add "pyocclient @ git+https://github.com/brozkeff/pyocclient.git@v0.6+brozkeff.20260622.sha.a33ddcbb.r1"
```

## Usage

Existing code should continue to import `owncloud`:

```python
import owncloud

oc = owncloud.Client("https://cloud.example.com/owncloud")
oc.login("user", "password")
```

## Versioning

Fork builds use PEP 440 local versions based on upstream `0.6`:

```text
0.6+brozkeff.YYYYMMDD.sha.UPSTREAMHASH.rREVISION
```

Example:

```text
0.6+brozkeff.20260622.sha.a33ddcbb.r1
```

This keeps the fork clearly tied to the official 0.6 release while allowing
multiple non-maintainer updates.

## Upstream Provenance

The official upstream source is recorded in `source/upstream/pypi-url.txt`.
The current fork baseline is:

- Project: <https://pypi.org/project/pyocclient/>
- Source: <https://files.pythonhosted.org/packages/1f/ce/c60f248822f4a4cc922a2766714e884a2eced5d8fc06a26ffe875ae1de09/pyocclient-0.6.tar.gz>
- Version: `0.6`
- Release date: 2020-09-17
- SHA256 prefix used in fork version: `a33ddcbb`

## Maintenance Changes

- Add `pyproject.toml` with PEP 517 build metadata so modern `pip` and `uv`
  do not fall back to legacy `setup.py bdist_wheel`.
- Fix Python 3.12 invalid escape `SyntaxWarning` messages in docstrings.
- Declare this fork as Python 3-only maintenance metadata.

The original integration tests require a configured live ownCloud instance.
For local compatibility checks, build the package and verify import:

```bash
uv build
uv run python -m compileall owncloud
uv run python -c "import importlib.metadata as m; import owncloud; print(m.version('pyocclient'))"
```

