"""Offline regression tests for error-body handling."""

import unittest

import requests

from owncloud import HTTPResponseError, OCSResponseError


class ResponseErrorTests(unittest.TestCase):
    def test_integer_status_has_no_body(self) -> None:
        for error_type in (HTTPResponseError, OCSResponseError):
            with self.subTest(error_type=error_type.__name__):
                error = error_type(404)
                self.assertEqual(error.status_code, 404)
                self.assertIn("404", str(error))
                self.assertIsNone(error.get_resource_body())

    def test_http_body_is_preserved_even_for_error_response(self) -> None:
        response = self.response(b"Not found")
        error = HTTPResponseError(response)
        self.assertIs(error.res, response)
        self.assertEqual(error.status_code, 404)
        self.assertEqual(error.get_resource_body(), b"Not found")

    def test_ocs_message_bytes_are_decoded(self) -> None:
        error = OCSResponseError(self.response(
            '<message>Accès refusé &amp; denied</message>'.encode("utf-8")
        ))
        self.assertEqual(error.get_resource_body(), "Accès refusé & denied")

    def test_ocs_non_xml_body_is_preserved(self) -> None:
        for body in (b"Bad gateway", b"<message>truncated", b""):
            with self.subTest(body=body):
                error = OCSResponseError(self.response(body))
                self.assertEqual(error.get_resource_body(), body)

    @staticmethod
    def response(body: bytes) -> requests.Response:
        response = requests.Response()
        response.status_code = 404
        response._content = body
        return response
