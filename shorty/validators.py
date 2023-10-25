import re
from shorty.errors import ShortlinksValidationError

PROVIDERS = ["", 'bitly', 'tinyurl']


class Validator:

    @staticmethod
    def validate_url(url: str):
        valid_url = re.match(
            r"(https?|ftp)://"  # protocol
            r"(\w+(\-\w+)*\.)?"  # host (optional)
            r"((\w+(\-\w+)*)\.(\w+))"  # domain
            r"(\.\w+)*"  # top-level domain (optional, can have > 1)
            r"([\w\-\._\~/]*)*(?<!\.)",  # path, params, anchors, etc.
            url)
        if not valid_url:
            raise ShortlinksValidationError("Invalid URL", 422)
        return True

    @staticmethod
    def validate_url_provider(provider: str):
        if provider not in PROVIDERS:
            raise ShortlinksValidationError("Invalid URL provider", 422)
        return True
