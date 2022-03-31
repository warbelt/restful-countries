from flask_restful_countries.model import sqlite_connector as db


def get_countries_list():
    country_names = db.execute_query("""
        SELECT name
        FROM countries
    """)

    return country_names


def get_country_data(name: str):
    """
    Returns a single row with fields name, iso2, iso3 for country with name that matches
    """
    country_data = db.execute_query(
        """
            SELECT name, iso2, iso3
            FROM countries
            WHERE name=?
        """,
        args=[name],
        one=True
    )

    return country_data


def insert_country(name: str, iso2: str, iso3: str):
    """
    Inserts a new row into database with fields name, iso2, iso3
    """
    db.execute_query(
        """
            INSERT INTO countries (name, iso2, iso3)
            VALUES (?,?,?)
        """,
        args=[name, iso2, iso3],
        one=True
    )
    db.commit_transaction()
