from datetime import datetime
from app.extensions import db


class Plate(db.Model):
    """This is the table for number plates"""
    __tablename__ = 'plates'

    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(50), unique=True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, plate_number):
        self.plate_number = plate_number

    def __repr__(self):
        return f"{self.plate_number}"
