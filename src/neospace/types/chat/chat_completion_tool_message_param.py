# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Optional, Required, TypedDict

from neospace.types.chat.chat_completion_tool_error_param import ChatCompletionToolError

__all__ = ["ChatCompletionToolMessageParam"]


class ChatCompletionToolMessageParam(TypedDict, total=False):
    content: Required[str]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""

    tool_error: Optional[ChatCompletionToolError]
    """
    Error object if the message is an error message. If this is present, the message should be treated as an error message.
    """
