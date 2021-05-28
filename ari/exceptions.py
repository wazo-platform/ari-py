from requests import RequestException


class ARIException(RequestException):
    def __init__(self, ari_client, original_error):
        self.client = ari_client
        self.original_error = original_error


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
