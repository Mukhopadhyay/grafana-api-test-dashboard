from typing import Optional

class Error(Exception):
    """Base class for exceptions in this module"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class GrafanaHTTPError(Error):
    """Exception raised because of the Grafana HTTP API"""
    def __init__(self, message: str, status_code: int, data: Optional[dict] = None, headers: Optional[dict] = None) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.data = data
        self.headers = headers

    def __str__(self) -> str:
        return self.message
