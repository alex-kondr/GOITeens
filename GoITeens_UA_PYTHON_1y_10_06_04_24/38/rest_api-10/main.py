from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api

import db_actions
from db import create_db


app = Flask(__name__)
api = Api(app)


def row_to_data(quotes: list):
    response_data = []
    for quote in quotes:
        response_data.append({
            "id": quote.id,
            "author": quote.author,
            "text": quote.text
        })

    response_data = jsonify(response_data)
    response_data.status_code = 200
    return response_data


class QuoteAPI(Resource):
    def get(self, id=None):
        if id:
            quote = db_actions.get_quote(id)
            if quote:
                return row_to_data([quote])
            else:
                response = jsonify(f"Цитата з id '{id}' відсутня")
                response.status_code = 404
                return response

        quotes = db_actions.get_quotes()
        if quotes:
            return row_to_data(quotes)
        else:
            response = jsonify("Цитати відсутні")
            response.status = 404
            return response

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        params = parser.parse_args()
        quote_id = db_actions.add_quote(params.get("author"), params.get("text"))
        response = jsonify(f"Цитата успішно додана під id '{quote_id}'")
        response.status_code = 200
        return response

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        params = parser.parse_args()
        message = db_actions.update_quote(id, params.get("author"), params.get("text"))
        response = jsonify(message)
        response.status_code = 200
        return response

    def delete(self, id):
        message = db_actions.delete_quote(id)
        response = jsonify(message)
        response.status_code = 200
        return response


api.add_resource(QuoteAPI, "/api/quotes/", "/api/quotes/<int:id>/")


if __name__ == "__main__":
    create_db()
    app.run(port=3000)