from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from db import create_db



app = Flask(__name__)
api = Api(app)
CORS(app)


class Post(Resource):
    def get(self, id=0):
        if id:
            post = get_post(id)
            post_json = row_to_json([post])
            return post_json


def row_to_json(posts: list):
    data = []
    for post in posts:
        data.append({
            "id": post.id,
            "author": post.author,
            "post": post.text
        })
    data_json = jsonify(data)
    data_json.status_code = 200
    return data_json


api.add_resource(Post, "/api/posts/", "/api/posts/<int:id>/")


if __name__ == "__main__":
    create_db()
    app.run(post=80, debug=True)
