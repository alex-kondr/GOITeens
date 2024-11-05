from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from app.db.db import delete_quote, get_quotes, get_quote, limit, add_quote, update_quote, delete_quote
from app.db.base import create_db

app = Flask(__name__)
api = Api(app)
CORS(app)

SWAGGER_URL = "/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
   SWAGGER_URL,
   API_URL,
   config={
       'app_name': 'Access API'
   }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

class Quote(Resource):
    def get(self, id=0):
        if not id:
            quotes = get_quotes()
            quote_json = row_to_json(quotes)
            return quote_json

        quote = get_quote(id)
        if quote:
            quote_json = row_to_json([quote])
            return quote_json

        return "Цитати не знайдені", 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        answer = add_quote(params.get("author"), params.get("quote"))
        json_data = jsonify(f"Цитату додано під id {answer}")
        json_data.status_code = 201
        return json_data

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        update_quote(id, params.get("author"), params.get("quote"))
        json_data = jsonify(f"Цитату id {id} успішно оновлено")
        json_data.status_code = 202
        return json_data

    def delete(self, id):
        delete_quote(id)
        json_data = jsonify(f"Цитату id {id} успішно видалено")
        json_data.status_code = 200
        return json_data


def row_to_json(quotes: list):
    data = []
    for quote in quotes:
        data.append({
            "id": quote.id,
            "author": quote.author,
            "quote": quote.quote
        })
    json_data = jsonify(data)
    json_data.status_code = 200
    return json_data


api.add_resource(Quote, "/api/v1.0/quotes/", "/api/v1.0/quotes/<int:id>/")


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
