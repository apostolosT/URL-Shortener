from flask import jsonify


class ShortlinksValidationError(Exception):
    status_code = 422

    def __init__(self, message: str, status_code: int = None, payload: dict = None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.stack = ""

    def to_dict(self):
        return jsonify({
            'error': {
                'statusCode': self.status_code,
                'name': "ShortlinksValidationError",
                'message': self.message
            }
        })


class UrlProviderError(Exception):
    status_code = 503

    def __init__(self, message: str, status_code: int = None, payload: dict = None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.stack = ""

    def to_dict(self):
        return jsonify({
            'error': {
                'statusCode': self.status_code,
                'name': "UrlProviderError",
                'message': self.message
            }
        })


def export_errors():
    return (
        ShortlinksValidationError
    )
