from importlib.resources import path
import sqlite3
import os
import csv


COUNTRIES_DATABASE = 'countries.sqlite3'
COUNTRY_CODES_FILE = 'country_codes.csv'


def install_db():
    # This will create the database if it is not created yet
    con = sqlite3.connect(COUNTRIES_DATABASE)

    # Drop table if exsits, then create table
    con.execute("""
        DROP TABLE IF EXISTS countries
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS countries (name, iso2, iso3)
    """)

    # Load countries list from csv
    countries_csv = os.path.join(os.path.dirname(__file__), COUNTRY_CODES_FILE)
    with open(countries_csv, 'r') as f:
        countries = [row for row in csv.DictReader(f, delimiter=',')]

    # Insert country data in database
    for row in countries:
        con.execute("""
            INSERT INTO countries (name, iso2, iso3)
            VALUES (?, ?, ?)
        """, (row['name'], row['iso2'], row['iso3']))

    con.commit()

    records = con.execute("""
        SELECT COUNT(*) FROM countries
    """).fetchall()[0][0]
    print(f"Created table 'countries' in database {COUNTRIES_DATABASE} with {records} records.")

    con.close()


if __name__ == '__main__':
    install_db()
