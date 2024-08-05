# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Optional, Required, TypedDict

__all__ = ["ChatCompletionToolError"]


class ChatCompletionToolError(TypedDict, total=False):
    status: Required[str]
    """
    The status of the error. Can be any you want, but for best usage use descriptive names like `X_SERVICE_ERROR`, etc.
    """
    code: Optional[str]
    """
    The error code, if available. Can be any you want, but for best usage use descriptive codes like 4xx, 5xx or any code you want.
    """
    message: Optional[str]
    """
    The error message, if available. Can be any you want, but for best usage use descriptive messages like `Service Unavailable`, etc.
    """
