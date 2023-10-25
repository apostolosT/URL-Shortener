from shorty.providers import UrlProvider, BitlyUrlProvider, TinyUrlProvider

PROVIDERS = ["bitly", "tinyurl"]


def get_url_provider(url_provider: str) -> UrlProvider:
    factories = {
        "bitly": BitlyUrlProvider(),
        "tinyurl": TinyUrlProvider()
    }
    if url_provider in factories:
        return factories[url_provider]
    return BitlyUrlProvider()
