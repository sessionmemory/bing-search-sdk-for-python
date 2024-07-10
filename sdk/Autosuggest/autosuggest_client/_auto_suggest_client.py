# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer


if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import AutoSuggestClientConfiguration
from .operations import AutoSuggestClientOperationsMixin
import models


class AutoSuggestClient(AutoSuggestClientOperationsMixin):
    """Autosuggest supplies search terms derived from a root text sent to the service.  The terms Autosuggest supplies are related to the root text based on similarity and their frequency or ratings of usefulness in other searches. For examples that show how to use Autosuggest, see `Search using AutoSuggest <https://docs.microsoft.com/en-us/bing/bing-autosuggest/overview>`_.

    :param credential: Credential needed for the client to connect to Azure.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: none
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "https://api.bing.microsoft.com/v7.0"
        self._config = AutoSuggestClientConfiguration(credential, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)
        client_models = {
            k: v for k, v in models.__dict__.items() if isinstance(v, type)
        }
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoSuggestClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
