# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os as _os

import httpx
import pytest
from httpx import URL

import neospace
from neospace import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES


def reset_state() -> None:
    neospace._reset_client()
    neospace.api_key = None or "My API Key"
    neospace.organization = None
    neospace.project = None
    neospace.base_url = None
    neospace.timeout = DEFAULT_TIMEOUT
    neospace.max_retries = DEFAULT_MAX_RETRIES
    neospace.default_headers = None
    neospace.default_query = None
    neospace.http_client = None
    neospace.api_type = _os.environ.get("NEOSPACE_API_TYPE")  # type: ignore
    neospace.api_version = None
    neospace.azure_endpoint = None
    neospace.azure_ad_token = None
    neospace.azure_ad_token_provider = None


@pytest.fixture(autouse=True)
def reset_state_fixture() -> None:
    reset_state()


def test_base_url_option() -> None:
    assert neospace.base_url is None
    assert neospace.completions._client.base_url == URL("https://api.neospace.com/v1/")

    neospace.base_url = "http://foo.com"

    assert neospace.base_url == URL("http://foo.com")
    assert neospace.completions._client.base_url == URL("http://foo.com")


def test_timeout_option() -> None:
    assert neospace.timeout == neospace.DEFAULT_TIMEOUT
    assert neospace.completions._client.timeout == neospace.DEFAULT_TIMEOUT

    neospace.timeout = 3

    assert neospace.timeout == 3
    assert neospace.completions._client.timeout == 3


def test_max_retries_option() -> None:
    assert neospace.max_retries == neospace.DEFAULT_MAX_RETRIES
    assert neospace.completions._client.max_retries == neospace.DEFAULT_MAX_RETRIES

    neospace.max_retries = 1

    assert neospace.max_retries == 1
    assert neospace.completions._client.max_retries == 1


def test_default_headers_option() -> None:
    assert neospace.default_headers == None

    neospace.default_headers = {"Foo": "Bar"}

    assert neospace.default_headers["Foo"] == "Bar"
    assert neospace.completions._client.default_headers["Foo"] == "Bar"


def test_default_query_option() -> None:
    assert neospace.default_query is None
    assert neospace.completions._client._custom_query == {}

    neospace.default_query = {"Foo": {"nested": 1}}

    assert neospace.default_query["Foo"] == {"nested": 1}
    assert neospace.completions._client._custom_query["Foo"] == {"nested": 1}


def test_http_client_option() -> None:
    assert neospace.http_client is None

    original_http_client = neospace.completions._client._client
    assert original_http_client is not None

    new_client = httpx.Client()
    neospace.http_client = new_client

    assert neospace.completions._client._client is new_client


import contextlib
from typing import Iterator

from neospace.lib.azure import AzureNeoSpace


@contextlib.contextmanager
def fresh_env() -> Iterator[None]:
    old = _os.environ.copy()

    try:
        _os.environ.clear()
        yield
    finally:
        _os.environ.clear()
        _os.environ.update(old)


def test_only_api_key_results_in_neospace_api() -> None:
    with fresh_env():
        neospace.api_type = None
        neospace.api_key = "example API key"

        assert type(neospace.completions._client).__name__ == "_ModuleClient"


def test_azure_api_key_env_without_api_version() -> None:
    with fresh_env():
        neospace.api_type = None
        _os.environ["AZURE_NEOSPACE_API_KEY"] = "example API key"

        with pytest.raises(
            ValueError,
            match=r"Must provide either the `api_version` argument or the `NEOSPACE_API_VERSION` environment variable",
        ):
            neospace.completions._client  # noqa: B018


def test_azure_api_key_and_version_env() -> None:
    with fresh_env():
        neospace.api_type = None
        _os.environ["AZURE_NEOSPACE_API_KEY"] = "example API key"
        _os.environ["NEOSPACE_API_VERSION"] = "example-version"

        with pytest.raises(
            ValueError,
            match=r"Must provide one of the `base_url` or `azure_endpoint` arguments, or the `AZURE_NEOSPACE_ENDPOINT` environment variable",
        ):
            neospace.completions._client  # noqa: B018


def test_azure_api_key_version_and_endpoint_env() -> None:
    with fresh_env():
        neospace.api_type = None
        _os.environ["AZURE_NEOSPACE_API_KEY"] = "example API key"
        _os.environ["NEOSPACE_API_VERSION"] = "example-version"
        _os.environ["AZURE_NEOSPACE_ENDPOINT"] = "https://www.example"

        neospace.completions._client  # noqa: B018

        assert neospace.api_type == "azure"


def test_azure_azure_ad_token_version_and_endpoint_env() -> None:
    with fresh_env():
        neospace.api_type = None
        _os.environ["AZURE_NEOSPACE_AD_TOKEN"] = "example AD token"
        _os.environ["NEOSPACE_API_VERSION"] = "example-version"
        _os.environ["AZURE_NEOSPACE_ENDPOINT"] = "https://www.example"

        client = neospace.completions._client
        assert isinstance(client, AzureNeoSpace)
        assert client._azure_ad_token == "example AD token"


def test_azure_azure_ad_token_provider_version_and_endpoint_env() -> None:
    with fresh_env():
        neospace.api_type = None
        _os.environ["NEOSPACE_API_VERSION"] = "example-version"
        _os.environ["AZURE_NEOSPACE_ENDPOINT"] = "https://www.example"
        neospace.azure_ad_token_provider = lambda: "token"

        client = neospace.completions._client
        assert isinstance(client, AzureNeoSpace)
        assert client._azure_ad_token_provider is not None
        assert client._azure_ad_token_provider() == "token"
