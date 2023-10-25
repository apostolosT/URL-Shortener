import os
import requests
from shorty.errors import UrlProviderError


class UrlProvider:
    def shorten(self):
        pass


class BitlyUrlProvider(UrlProvider):
    """
    Bitly Api Wrapper
    """
    BITLY_TOKEN = os.getenv('BITLY_TOKEN')  # or replace with your own token

    def shorten(self, url):
        bitly_endpoint = "https://api-ssl.bitly.com/v4/shorten"
        headers = {
            "Authorization": f"Bearer {self.BITLY_TOKEN}",
            "Content-Type": "application/json"
        }
        body = {
            "long_url": url
        }
        try:
            response = requests.post(
                bitly_endpoint,
                json=body,
                headers=headers
            )
            data = response.json()
            return data.get('link', None)
        # TODO: better error handling for different requests exceptions
        except Exception:
            message = "bitly provider unavailable"
            raise UrlProviderError(message)


class TinyUrlProvider(UrlProvider):
    """
    TinyUrl Api Wrapper
    """
    def shorten(self, url):
        tiny_url_endpoint = 'https://api.tinyurl.com/create'
        headers = {
            "Authorization": f"Bearer {os.getenv('TINYURL_TOKEN')}",
            "Content-Type": "application/json"
        }
        body = {
            "url": url
        }
        try:
            response = requests.post(
                tiny_url_endpoint,
                json=body,
                headers=headers
            )

            data = response.json()
            return data.get('tiny_url', None)
        # TODO: better error handling for different requests exceptions
        except Exception:
            message = "tinyurl provider unavailable"
            raise UrlProviderError(message)
