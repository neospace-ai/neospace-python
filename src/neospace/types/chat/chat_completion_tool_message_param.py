# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionToolMessageParam"]


class ChatCompletionToolMessageParam(TypedDict, total=False):
    content: Required[str]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""

    status: Literal["SUCCESS", "SERVER_ERROR", "CLIENT_ERROR"]
    """
    The status of the tool message. `SUCCESS` if the tool message was successful (200), 
    `SERVER_ERROR` if the tool message was unsuccessful due to a server error (500), 
    or `CLIENT_ERROR` if the tool message was unsuccessful due to a client error (400).
    """
