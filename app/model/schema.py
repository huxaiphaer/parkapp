from marshmallow import fields

from app.extensions import ma, db
from app.model.plate import Plate


class PlateSchema(ma.SQLAlchemySchema):
    """Plates Schema for the model."""

    class Meta:
        model = Plate
        sqla_session = db.session

    plate_number = fields.String(required=True)
    time_stamp = fields.DateTime()


