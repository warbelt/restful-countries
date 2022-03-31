### Testing poetry, pluggable views, flask-restful and sqlite3
---
## Installation
1. Clone this repository
2. Install [poetry](https://python-poetry.org/)
3. Install the project's dependencies with `poetry install`
4. Create a fresh sqlite3 db with some examples with `poetry run install_db`

## Running the server
*Note: It is encouraged to have install the database first by following the installation process.*

## API
`GET /countries/`

Returns an array of existing country names in the database

`GET /countries/<str:country_name>`

Returns a document containing the iso2 and iso3 translations for the requested country, if it exists in the database.

`POST /countries/`

```
PARAM str country
PARAM str iso2
PARAM str iso3
```

Inserts a new country into the database with the values specified in the URL string parameters


## Examples
### Get all names
http://127.0.0.1:5000/countries/

### Get data for country "france"
http://127.0.0.1:5000/countries/france

### Insert iso2 and iso3 data for country "china"
http://127.0.0.1:5000/countries?country=china&iso2=cn&iso3=chn