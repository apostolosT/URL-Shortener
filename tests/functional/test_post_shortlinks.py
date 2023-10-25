VALID_URL = "http://www.example.com"
INVALID_URL = "testopoulos .com"
VALID_PROVIDER = "bitly"
INVALID_PROVIDER = "testopoulos"


class TestApi:
    def test_shortlinks_invalid_url(self, client):
        body = {
            'url': INVALID_URL,
            'provider': VALID_PROVIDER
        }
        response = client.post('/shortlinks', json=body)
        assert response.status_code == 422
        assert response.json['error']['message'] == 'Invalid URL'
        assert response.json['error']['name'] == 'ShortlinksValidationError'

    def test_shortlinks_invalid_provider(self, client):
        body = {
            'url': VALID_URL,
            'provider': INVALID_PROVIDER
        }
        response = client.post('/shortlinks', json=body)
        assert response.status_code == 422
        assert response.json['error']['message'] == 'Invalid URL provider'
        assert response.json['error']['name'] == 'ShortlinksValidationError'

    def test_shortlinks_empty_provider(self, client, shorty_response_stub):
        body = {
            'url': VALID_URL,
            'provider': ""
        }
        response = client.post('/shortlinks', json=body)
        assert response.status_code == 200
        assert response.get_json()

    def test_shortlinks_valid_input(self, client, shorty_response_stub):
        body = {
            'url': VALID_URL,
            'provider': VALID_PROVIDER
        }
        response = client.post('/shortlinks', json=body)
        assert response.status_code == 200
        assert response.get_json()
