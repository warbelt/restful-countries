from flask import Flask
from flask_restful_countries.views import countries_views

app = Flask(__name__)


def register_urls(app):
    countries_view = countries_views.ShowCountries.as_view('show_countries')
    app.add_url_rule("/countries/",
                    defaults={'country_name': "1234"},
                    view_func=countries_view,
                    methods=["GET"])

    app.add_url_rule("/countries/<string:country_name>",
                    view_func=countries_view,
                    methods=["GET"])

    app.add_url_rule("/countries/",
                    view_func=countries_view,
                    methods=["POST"])


@app.route("/")
def helloworld():
    return {'hello': 'world'}


def main():
    app.run()


if __name__ == '__main__':
    register_urls(app)
    main()

register_urls(app)