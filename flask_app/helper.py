from flask import abort
import db
import validator


def get_codes(origin_or_dest, code_or_slug):
    """ gets the codes for the given code or slug. """
    code_or_slug = validator.check_code_or_slug_case(code_or_slug)
    if len(code_or_slug) > 5:
        port_codes = db.query_get_region_port_codes(code_or_slug)
    else:
        port_codes = db.query_validate_port_codes(code_or_slug)
    return construct_codes(origin_or_dest, port_codes)


def get_average_price(date_from, date_to, origin_codes, destination_codes):
    """ gets the average prices for the given parameters. """
    average_prices = db.query_get_average_prices(date_from, date_to, origin_codes, destination_codes)
    return construct_average_prices(average_prices)


def construct_codes(origin_or_dest, codes):
    """ Constructs the list of tuples [('NLRTM',), ('BEZEE',)] to a simple tuple ('NLRTM', 'BEZEE'). """
    return tuple(code[0] for code in codes) if codes else abort(400, f'- given {origin_or_dest} does not exist')


def construct_average_prices(res):
    """ Constructs the result of average prices to a {'day': day, 'average_price': average_price} format. """
    return [{'day': str(day), 'average_price': average_price} for day, average_price in res]




