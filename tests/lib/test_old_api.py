import pytest

import neospace
from neospace.lib._old_api import APIRemovedInV1


def test_basic_attribute_access_works() -> None:
    for attr in dir(neospace):
        dir(getattr(neospace, attr))


def test_helpful_error_is_raised() -> None:
    with pytest.raises(APIRemovedInV1):
        neospace.Completion.create()  # type: ignore

    with pytest.raises(APIRemovedInV1):
        neospace.ChatCompletion.create()  # type: ignore
