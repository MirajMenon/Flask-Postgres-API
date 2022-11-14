from datetime import datetime
from flask import abort

# Format of the date YYYY-MM-DD
DATE_FORMAT = '%Y-%m-%d'


def validate_params(date_from, date_to, origin, destination):
    """ Checks all the validations of the parameters. """
    is_not_empty = check_empty(date_from, date_to, origin, destination)
    is_valid_format = check_date_format(date_from, date_to)
    is_valid_diff = check_date_diff(date_from, date_to)
    return True if is_not_empty and is_valid_format and is_valid_diff else abort(400)


def check_empty(date_from, date_to, origin, destination):
    """ Checks if any parameters are empty. """
    if date_from and date_to and origin and destination:
        return True
    else:
        abort(400, '- please enter all the parameters')


def check_date_format(date_from, date_to):
    """ Checks if date formats are correct. """
    try:
        if bool(datetime.strptime(date_from, DATE_FORMAT)) and bool(datetime.strptime(date_to, DATE_FORMAT)):
            return True
    except ValueError:
        abort(400, '- incorrect date format, should be YYYY-MM-DD')


def check_date_diff(date_from, date_to):
    """ Checks if the difference between date_from and date_to are correct. """
    if datetime.strptime(date_from, DATE_FORMAT) <= datetime.strptime(date_to, DATE_FORMAT):
        return True
    else:
        abort(400, '- incorrect date range, date_from is greater than date_to')


def check_code_or_slug_case(code_or_slug):
    """ Checks the case of the port code or region slug, and returns the correct case format. """
    return code_or_slug.upper() if len(code_or_slug) == 5 else code_or_slug.lower()
