import pytest
import shorty


@pytest.fixture(scope='function')
def shorty_response_stub(monkeypatch):
    """
    Stubs shorty
    """
    def shorten_url_mock(*args, **kwargs):
        return {
            "link": "https://bit.ly/8h1bka",
            "url": "https://example.com"
        }
    monkeypatch.setattr(shorty.shorty.Shorty, 'shorten_url_with_retry', shorten_url_mock)


@pytest.fixture(scope='function')
def bitly_response_stub(monkeypatch):
    """
    Stubs bitly provider shortened response
    """
    def bitly_shorten_mock(*args, **kwargs):
        return "https://bit.ly/abcdef"

    monkeypatch.setattr(
        shorty.providers.BitlyUrlProvider,
        'shorten',
        bitly_shorten_mock)


@pytest.fixture()
def tinyurl_response_stub(monkeypatch):
    """
    Stubs bitly provider shortened response
    """
    def tiny_url_shorten_mock(*args, **kwargs):
        return "https://tinyurl.com/abcdef"

    monkeypatch.setattr(
        shorty.providers.TinyUrlProvider,
        'shorten',
        tiny_url_shorten_mock)
