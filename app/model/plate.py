from app.extensions import db


class Plate(db.Model):
    """This is the table for number plates"""
    __tablename__ = 'plates'

    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(50))
