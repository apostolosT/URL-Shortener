import logging
from flask import Blueprint, jsonify, request
from pyparsing import traceback
from shorty.shorty import Shorty
from shorty.errors import export_errors

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    """
    file: swagger/post_shortlinks.yaml
    """
    request_body = request.get_json()
    shorty = Shorty(request_body)
    response = shorty.shorten_url_with_retry()
    return jsonify(response), 200


@api.errorhandler(Exception)
def handle_error(e):
    logging.error(str(e), exc_info=1)
    if isinstance(e, export_errors()):
        if hasattr(e, 'status_code'):
            e.stack = traceback.format_exc()
            response = e.to_dict()
            response.status_code = e.status_code
            return response
        return jsonify({
            'error': {
                'statusCode': 400,
                'name': type(e).__name__,
                'message': repr(e),
                'stack': traceback.format_exc()
            }
        })

    raise e
