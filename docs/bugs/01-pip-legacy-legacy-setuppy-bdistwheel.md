# legacy setup.py bdist_wheel incompatible with newer Pip

source: <https://github.com/tierraverde-cz/pracovnipostupator/issues/27>

Pip warns during install

```text
Building wheels for collected packages: pyocclient
  DEPRECATION: Building 'pyocclient' using the legacy setup.py bdist_wheel mechanism, which will be removed in a future version. pip 25.3 will enforce this behaviour change. A possible replacement is to use the standardized build interface by setting the `--use-pep517` option, (possibly combined with `--no-build-isolation`), or adding a `pyproject.toml` file to the source tree of 'pyocclient'. Discussion can be found at https://github.com/pypa/pip/issues/6334
```

Temporary workaround currently used: pin pip in requirements.in

```pip
pip<25.3
pyocclient==0.6
```

Need making new proper pyproject for newer pip compatibility.
