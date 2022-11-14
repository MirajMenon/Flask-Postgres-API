from requests import get

URL = 'http://127.0.0.1/rates'


def test_expected_result():
    expected = [
        {"day": "2016-01-01", "average_price": 1112},
        {"day": "2016-01-02", "average_price": 1112},
        {"day": "2016-01-04", "average_price": None},
        {"day": "2016-01-05", "average_price": 1142},
        {"day": "2016-01-06", "average_price": 1142},
        {"day": "2016-01-07", "average_price": 1137},
        {"day": "2016-01-08", "average_price": 1124},
        {"day": "2016-01-09", "average_price": 1124},
        {"day": "2016-01-10", "average_price": 1124}
    ]
    str_params = "?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 200
    assert res.json() == expected


def test_empty_inputs():
    str_params = "?date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 400
    assert res.json() == {'Error': 'Bad request - please enter all the parameters'}


def test_incorrect_date_format():
    str_params = "?date_from=7777-77-77&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 400
    assert res.json() == {'Error': 'Bad request - incorrect date format, should be YYYY-MM-DD'}


def test_incorrect_date_difference():
    str_params = "?date_from=2017-01-01&date_to=2016-01-01&origin=CNSGH&destination=north_europe_main"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 400
    assert res.json() == {'Error': 'Bad request - incorrect date range, date_from is greater than date_to'}


def test_incorrect_origin():
    str_params = "?date_from=2016-01-01&date_to=2016-01-01&origin=INCORRECT&destination=north_europe_main"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 400
    assert res.json() == {"Error": "Bad request - given origin does not exist"}


def test_incorrect_destination():
    str_params = "?date_from=2016-01-01&date_to=2016-01-01&origin=CNSGH&destination=INCORRECT"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 400
    assert res.json() == {"Error": "Bad request - given destination does not exist"}


def test_origin_lower_case():
    str_params = "?date_from=2016-01-01&date_to=2016-01-01&origin=cnsgh&destination=north_europe_main"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 200


def test_destination_upper_case():
    str_params = "?date_from=2016-01-01&date_to=2016-01-01&origin=cnsgh&destination=NORTH_EUROPE_MAIN"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 200


def test_sql_injection():
    str_params = "?date_from=2016-01-01&date_to=2016-01-01&origin=CNSGH') OR 1=1;--&destination=NORTH_EUROPE_MAIN"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 400
    assert res.json() == {"Error": "Bad request - given origin does not exist"}


def test_response_404():
    str_params = "?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
    res = get(f"{URL}ABC{str_params}")
    assert res.status_code == 404
    assert res.json() == {'Error': 'Not found'}


def test_both_port_codes():
    expected = [
        {"day": "2016-01-01", "average_price": 882},
        {"day": "2016-01-02", "average_price": 882},
        {"day": "2016-01-05", "average_price": 882},
        {"day": "2016-01-06", "average_price": 882},
        {"day": "2016-01-07", "average_price": 882},
        {"day": "2016-01-08", "average_price": 832},
        {"day": "2016-01-09", "average_price": 832},
        {"day": "2016-01-10", "average_price": 832}
    ]
    str_params = "?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=NLRTM"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 200
    assert res.json() == expected


def test_both_region_slugs():
    expected = [
        {"day": "2016-01-01", "average_price": 1174},
        {"day": "2016-01-02", "average_price": 1174},
        {"day": "2016-01-04", "average_price": None},
        {"day": "2016-01-05", "average_price": 1214},
        {"day": "2016-01-06", "average_price": 1211},
        {"day": "2016-01-07", "average_price": 1201},
        {"day": "2016-01-08", "average_price": 1192},
        {"day": "2016-01-09", "average_price": 1192},
        {"day": "2016-01-10", "average_price": 1192}
    ]
    str_params = "?date_from=2016-01-01&date_to=2016-01-10&origin=china_east_main&destination=north_europe_main"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 200
    assert res.json() == expected


def test_region_slug_and_port_code():
    expected = [
        {"day": "2016-01-01", "average_price": 955},
        {"day": "2016-01-02", "average_price": 955},
        {"day": "2016-01-05", "average_price": 952},
        {"day": "2016-01-06", "average_price": 953},
        {"day": "2016-01-07", "average_price": 956},
        {"day": "2016-01-08", "average_price": 956},
        {"day": "2016-01-09", "average_price": 956},
        {"day": "2016-01-10", "average_price": 956}
    ]
    str_params = "?date_from=2016-01-01&date_to=2016-01-10&origin=china_east_main&destination=FRMTX"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 200
    assert res.json() == expected


def test_region_tree():
    expected = [
        {"day": "2016-01-01", "average_price": 1476},
        {"day": "2016-01-02", "average_price": 1476},
        {"day": "2016-01-04", "average_price": None},
        {"day": "2016-01-05", "average_price": 1463},
        {"day": "2016-01-06", "average_price": 1447},
        {"day": "2016-01-07", "average_price": 1429},
        {"day": "2016-01-08", "average_price": 1416},
        {"day": "2016-01-09", "average_price": 1423},
        {"day": "2016-01-10", "average_price": 1423}
    ]
    str_params = "?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=northern_europe"
    res = get(f"{URL}{str_params}")
    assert res.status_code == 200
    assert res.json() == expected
