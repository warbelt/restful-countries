from flask import Flask
from flask_restful_countries.views import countries_views

app = Flask(__name__)


@app.route("/")
def helloworld():
    return {'hello': 'world'}


def main():
    app.run()


if __name__ == '__main__':
    main()

app.add_url_rule("/countries", view_func=countries_views.ShowCountries.as_view('show_countries'))
