import sqlite3
from flask import g


COUNTRIES_DATABASE = 'countries.db'


def row_to_dict(cursor, row):
    return {
        cursor.description[idx][0] : value
        for idx, value in enumerate(row)
    }


def get_db() -> sqlite3.Connection:
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(COUNTRIES_DATABASE)
        db.row_factory = row_to_dict
    return db


def execute_query(query, args=(), one=False):
    cur = get_db().execute(query, args)

    query_results = cur.fetchall()
    cur.close()

    return query_results[0] if one else query_results
