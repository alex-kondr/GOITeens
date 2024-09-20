from flask import Flask

from app.routes.employee import employees_blueprint
from app.routes.position import positions_blueprint
from app.routes.cabinet import cabinets_blueprint
from app.routes.root import root_blueprint
from app.models.base import create_db
from app.models.associates import cabinet_position_assoc_table, employee_position_assoc_table
from app.models.cabinet import Cabinet
from app.models.employee import Employee
from app.models.position import Position


app = Flask(__name__)
app.register_blueprint(employees_blueprint)
app.register_blueprint(positions_blueprint)
app.register_blueprint(cabinets_blueprint)
app.register_blueprint(root_blueprint)

create_db()
