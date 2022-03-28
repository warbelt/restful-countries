import importlib.resources
import csv
from attr import field
from flask import request

from flask.views import MethodView

import flask_restful_countries.resources as module_resources


class ShowCountries(MethodView):
    methods = ["GET", "POST"]

    def get_all_countries(self):
        countries_csv = importlib.resources.files(module_resources).joinpath("country_codes.csv")
        with countries_csv.open('r') as f:
            countries = [row for row in csv.DictReader(f, delimiter=',')]
        return countries

    def get_country_data(self, name):
        countries_csv = importlib.resources.files(module_resources).joinpath("country_codes.csv")
        with countries_csv.open('r') as f:
            country_data = [row for row in csv.DictReader(f, delimiter=',') if row['name'] == name]

        if len(country_data) == 0:
            return None
        else:
            return country_data[0]

    def insert_country(self, name, iso2, iso3):
        countries_csv = importlib.resources.files(module_resources).joinpath("country_codes.csv")
        with countries_csv.open('r') as f:
            countries = csv.DictReader(f, delimiter=',')

        with countries_csv.open('a') as f:
            field_names = ["name", 'iso2', 'iso3']
            writer = csv.DictWriter(f, field_names)
            writer.writerow({
                'name': name,
                'iso2': iso2,
                'iso3': iso3
            })

    def get(self):
        request_country = request.args.get("country")

        country_data = self.get_country_data(request_country)
        if country_data:
            return {
                "name":request_country,
                "translations": {
                    "iso2": country_data["iso2"],
                    "iso3": country_data["iso3"]
                }
            }
        return f'Country "{request_country}" not found'

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
