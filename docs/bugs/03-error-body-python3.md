# Error-body inspection crashes on Python 3

## Reproduction

On revision r1, `HTTPResponseError(404).get_resource_body()` and
`OCSResponseError(404).get_resource_body()` raise `AttributeError` because
integer status codes leave the response attribute unset.

For an OCS response containing `b'<message>Access denied</message>'`,
`OCSResponseError(response).get_resource_body()` raises `TypeError` on
Python 3. `ElementTree.fromstringlist` iterates the bytes as integers instead
of parsing the response body as one XML document.

## Fix in r2

- Initialize the response attribute to `None` for integer status codes;
  body inspection returns `None` as intended.
- Parse the OCS body with `ElementTree.fromstring`, which accepts bytes.
  Message text is returned as a string; malformed XML still returns raw bytes.

Exception types, status codes, and HTTP body handling remain unchanged.
No dependencies or network behavior change. Offline regression tests are in
`tests/test_response_errors.py`.
