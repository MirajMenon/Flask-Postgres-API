import psycopg2
from os import environ
from flask import abort
import query


def execute_query(sql_query, params):
    """ Connects to the Postgres database server and executes the given query. """
    connection = None
    try:
        connection = psycopg2.connect(host=environ.get("POSTGRES_IP"),
                                      port='5432',
                                      database='postgres',
                                      user='postgres',
                                      password=environ.get("POSTGRES_PASSWORD"))
        cursor = connection.cursor()
        cursor.execute(sql_query, params)
        result = cursor.fetchall()
        cursor.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        abort(500)
    finally:
        if connection is not None:
            connection.close()


def query_get_region_port_codes(slug):
    """ Executes and get regions codes query and returns the port codes of region tree. """
    return execute_query(query.GET_REGION_TREE_CODES, (slug,))


def query_validate_port_codes(code):
    """ Executes and validate codes query and returns the port codes if its exists. """
    return execute_query(query.VALIDATE_CODES, (code,))


def query_get_average_prices(date_from, date_to, origin_codes, destination_codes):
    """ Executes the get average prices query. """
    params = (date_from, date_to, origin_codes, destination_codes)
    return execute_query(query.GET_AVERAGE_PRICES, params)
