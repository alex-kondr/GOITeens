from flask import Flask

from .routes.employee import employees_blueprint
from .routes.position import positions_blueprint
from .models import create_db, Session, Position


app = Flask(__name__)
app.register_blueprint(employees_blueprint, url_prefix="/employees/")
app.register_blueprint(positions_blueprint, url_prefix="/positions/")

# create_db()