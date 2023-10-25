import pytest
from shorty.shorty import Shorty
import shorty.errors
import shorty.providers


class TestShorty:
    def test_bitly_provider_selection(self, bitly_response_stub):
        init_params = {
            "url": "https://www.example.com",
            "provider": "bitly"
        }
        shortener = Shorty(init_params)
        assert "bitly" == shortener.provider_name
        response = shortener.shorten_url_with_retry()
        assert response['link'].startswith("https://bit.ly/")

    def test_bitly_shortener_raises_exception(self, mocker, tinyurl_response_stub):
        init_params = {
            "url": "https://www.example.com",
            "provider": "bitly"
        }

        mock_bitly_response = mocker.patch(
            'shorty.providers.BitlyUrlProvider.shorten')
        mock_bitly_response.side_effect = Exception()

        shortener = Shorty(init_params)

        res = shortener.shorten_url_with_retry()
        assert res

    def test_tinyurl_provider_selection(self, tinyurl_response_stub):
        init_params = {
            "url": "https://www.example.com",
            "provider": "tinyurl"
        }
        shortener = Shorty(init_params)
        assert "tinyurl" == shortener.provider_name
        response = shortener.shorten_url_with_retry()
        assert response['link'].startswith("https://tinyurl.com/")

    def test_tinyurl_shortener_raises_exception(self, mocker, bitly_response_stub):
        init_params = {
            "url": "https://www.example.com",
            "provider": "tinyurl"
        }
        shortener = Shorty(init_params)
        mock_tinyurl_response = mocker.patch(
            'shorty.providers.TinyUrlProvider.shorten')
        mock_tinyurl_response.side_effect = Exception()

        shortener = Shorty(init_params)

        res = shortener.shorten_url_with_retry()
        assert res

    def test_shorty_fallback_failure(self, mocker):
        init_params = {
            "url": "https://www.example.com",
            "provider": "tinyurl"
        }
        shortener = Shorty(init_params)
        mock_tinyurl_response = mocker.patch(
            'shorty.providers.TinyUrlProvider.shorten')
        mock_tinyurl_response.side_effect = Exception()
        mock_bitly_response = mocker.patch(
            'shorty.providers.BitlyUrlProvider.shorten')
        mock_bitly_response.side_effect = Exception()

        shortener = Shorty(init_params)

        with pytest.raises(shorty.errors.UrlProviderError):
            shortener.shorten_url_with_retry()
