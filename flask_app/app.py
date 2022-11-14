from flask import Flask, request, jsonify
from error_handler import error_handler
import validator
import helper

app = Flask(__name__)
app.register_blueprint(error_handler)
app.config['JSON_SORT_KEYS'] = False


@app.route('/rates', methods=['GET'])
def rates():
    """ Returns the day and its average prices in JSON format. """

    args = request.args.to_dict()
    date_from = args.get('date_from')
    date_to = args.get('date_to')
    origin = args.get('origin')
    destination = args.get('destination')

    is_valid = validator.validate_params(date_from, date_to, origin, destination)
    if is_valid:
        origin_codes = helper.get_codes('origin', origin)
        destination_codes = helper.get_codes('destination', destination)
        response = helper.get_average_price(date_from, date_to, origin_codes, destination_codes)
        return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
