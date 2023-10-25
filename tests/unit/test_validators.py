import pytest
from shorty.validators import Validator
import shorty.providers
import shorty.errors


class TestValidator:
    def test_valid_bitly_provider(self):
        provider = 'bitly'
        res = Validator.validate_url_provider(provider)
        assert res

    def test_valid_tinyurl_provider(self):
        provider = 'tinyurl'
        res = Validator.validate_url_provider(provider)
        assert res

    def test_invalid_provider(self):
        provider = 'testopoulidis'
        with pytest.raises(shorty.errors.ShortlinksValidationError):
            Validator.validate_url_provider(provider)

    def test_valid_url(self):
        url = 'http://www.google.com'
        res = Validator.validate_url(url)
        assert res

    def test_invalid_url(self):
        url = 'www.test.com'
        with pytest.raises(shorty.errors.ShortlinksValidationError):
            Validator.validate_url_provider(url)
