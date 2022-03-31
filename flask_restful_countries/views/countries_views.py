import importlib.resources
import csv
import sqlite3
from attr import field
from flask import request

from flask.views import MethodView

from flask_restful_countries.model import countries as countries_connector

class ShowCountries(MethodView):
    methods = ["GET", "POST"]

    def get_countries_list(self):
        countries = countries_connector.get_countries_list()

        return [country['name'] for country in countries]

    def get_country_data(self, name):
        country_data = countries_connector.get_country_data(name)

        return country_data

    def insert_country(self, name, iso2, iso3):
        countries_connector.insert_country(name, iso2, iso3)

    def get(self, country_name):
        if country_name is None:
            return {
                'name': self.get_countries_list()
            }

        else:
            country_data = self.get_country_data(country_name)
            if country_data:
                return {
                    "name":country_name,
                    "translations": {
                        "iso2": country_data["iso2"],
                        "iso3": country_data["iso3"]
                    }
                }
            return f'Country "{country_name}" not found'

    def post(self):
        name = request.args.get("country")
        iso2 = request.args.get("iso2")
        iso3 = request.args.get("iso3")

        if name and iso2 and iso3:
            self.insert_country(name, iso2, iso3)

        return {
            "name":name,
            "translations": {
                "iso2": iso2,
                "iso3": iso3
            }
        }
