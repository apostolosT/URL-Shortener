import pytest
import shorty.errors
from shorty.providers import BitlyUrlProvider, TinyUrlProvider


class TestProvider:

    def test_bitly_shorten_exception(self, mocker):
        mock_requests = mocker.patch('requests.post')
        mock_requests.side_effect = Exception()
        url = "https://www.example.com"
        bitly = BitlyUrlProvider()

        with pytest.raises(shorty.errors.UrlProviderError) as e:
            bitly.shorten(url)

        assert str(e.value.message) == 'bitly provider unavailable'

    def test_tinyurl_shorten_exception(self, mocker):
        mock_requests = mocker.patch('requests.post')
        mock_requests.side_effect = Exception()
        url = "https://www.example.com"
        tinyurl = TinyUrlProvider()

        with pytest.raises(shorty.errors.UrlProviderError) as e:
            tinyurl.shorten(url)

        assert str(e.value.message) == 'tinyurl provider unavailable'
