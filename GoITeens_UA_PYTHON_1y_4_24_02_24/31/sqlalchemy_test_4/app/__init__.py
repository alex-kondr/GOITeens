from flask import Flask

from app.routes.position import positions_route
from app.data.base import create_db
from app.data.position import Position
from app.data.employee import Employee


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.register_blueprint(positions_route)

create_db()
