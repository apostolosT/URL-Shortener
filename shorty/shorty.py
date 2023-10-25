import copy

import logging
from shorty.validators import Validator
from shorty.utils import get_url_provider, PROVIDERS
from shorty.errors import UrlProviderError


class Shorty:
    """
    This class handles all requests for shortening a url
    It's a facade for handling the various commponents implemented in other sets of classes
    """
    def __init__(self, req_params: dict) -> None:
        self.available_providers = copy.deepcopy(PROVIDERS)
        self.url = req_params.get('url', "")
        self.provider_name = req_params.get('provider', "")
        self.provider_name = self.provider_name.lower()
        self._validate_request_params()
        self.provider = self._get_url_provider()

    def shorten_url_with_retry(self):
        """
        Handles the shortening of the url.
        Supports a fallback strategy in case one of the providers is unavailable
        """
        max_retries = len(PROVIDERS)
        for i in range(max_retries):
            try:
                link = self.provider.shorten(self.url)
                response = {
                    'url': self.url,
                    'link': link
                }
                return response
            except Exception:
                self._hanle_unavailable_provider()

        raise UrlProviderError("All external url providers failed")

    # minimal implementation of a fallback mechanism
    def _hanle_unavailable_provider(self):
        """
        Helper method for recording available providers left after a failure
        """
        logging.warning(f"Failed fetching {self.provider_name} response")
        self.available_providers.remove(self.provider_name)
        if self.available_providers:
            self.provider_name = self.available_providers[0]
            logging.warning(f"Retrying fetching with {self.provider_name} api")
            self.provider = self._get_url_provider()

    def _get_url_provider(self):
        provider = get_url_provider(self.provider_name)
        return provider

    def _validate_request_params(self):
        """
        Validation of our init params
        """
        Validator.validate_url(self.url)
        Validator.validate_url_provider(self.provider_name)
