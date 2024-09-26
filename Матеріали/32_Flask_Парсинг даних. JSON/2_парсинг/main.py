from flask import Flask

from routes.pizza import root_router
from models.base import create_db
from models.pizza import Pizza
from models.ingredient import Ingredient


app = Flask(__name__)
app.register_blueprint(root_router)


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
