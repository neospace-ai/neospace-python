# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import override

from . import resources, _load_client
from ._utils import LazyProxy


class ChatProxy(LazyProxy[resources.Chat]):
    @override
    def __load__(self) -> resources.Chat:
        return _load_client().chat


class ModelsProxy(LazyProxy[resources.Models]):
    @override
    def __load__(self) -> resources.Models:
        return _load_client().models


class CompletionsProxy(LazyProxy[resources.Completions]):
    @override
    def __load__(self) -> resources.Completions:
        return _load_client().completions


chat: resources.Chat = ChatProxy().__as_proxied__()
models: resources.Models = ModelsProxy().__as_proxied__()
completions: resources.Completions = CompletionsProxy().__as_proxied__()
