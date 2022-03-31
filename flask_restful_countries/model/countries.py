from flask_restful_countries.model import sqlite_connector as db


def get_countries_list():
    country_names = db.execute_query("""
        SELECT name
        FROM countries
    """)

    return country_names