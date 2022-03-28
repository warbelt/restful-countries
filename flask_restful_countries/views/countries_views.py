import importlib.resources
import csv
from flask import request

from flask.views import View

import flask_restful_countries.resources as module_resources


class ShowCountries(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        if request.method == 'GET':
            request_country = request.args.get("country")

            countries_csv = importlib.resources.files(module_resources).joinpath("country_codes.csv")
            with countries_csv.open('r') as f:
                countries = csv.DictReader(f, delimiter=',')
                for row in countries:
                    if request_country and row["name"] == request_country:
                        response = {
                            "name":request_country,
                            "translations": {
                                "iso2": row["iso2"],
                                "iso3": row["iso3"]
                            }
                        }
                        return response

            return "Not found"
        elif request.method == 'POST':
            return "not implemented"