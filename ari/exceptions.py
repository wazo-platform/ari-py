import json

from requests import RequestException


class ARIException(RequestException):
    def __init__(self, ari_client, original_error):
        self.client = ari_client
        self.original_error = original_error
        self.original_message = self._extract_original_error_message(original_error)

    def _extract_original_error_message(self, original_error):
        try:
            return original_error.response.json().get('message')
        except (TypeError, AttributeError, json.JSONDecodeError):
            return


class ARIHTTPError(ARIException):
    pass


class ARINotFound(ARIHTTPError):
    pass


class ARINotInStasis(ARIHTTPError):
    pass


class ARIServerError(ARIHTTPError):
    pass


class ARIServerUnavailable(ARIHTTPError):
    pass
