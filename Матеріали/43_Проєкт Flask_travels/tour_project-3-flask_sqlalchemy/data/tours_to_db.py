from data.base import db
from data import data
from data.models_old import Tour


def data_to_db():
    for index, tour in data.tours.items():
        tour_db = Tour(id=index, **tour)
        db.session.add(tour_db)

    db.session.commit()