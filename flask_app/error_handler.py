from flask import Blueprint, jsonify

error_handler = Blueprint('error_handler', __name__)


@error_handler.app_errorhandler(400)
def handle_error_code_400(error):
    """ Handles the error code of 400. """
    return jsonify({'Error': f'Bad request {error.description}'}), 400


@error_handler.app_errorhandler(404)
def handle_error_code_404(error):
    """ Handles the error code of 404. """
    return jsonify({'Error': f'Not found'}), 404


@error_handler.app_errorhandler(500)
def handle_error_code_500(error):
    """ Handles the error code of 500. """
    return jsonify({'Error': f'Internal server error'}), 500
