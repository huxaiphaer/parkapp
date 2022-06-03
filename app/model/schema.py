from marshmallow import fields

from app.extensions import ma, db
from app.model.plate import Plate


class PlateSchema(ma.SQLAlchemySchema):
    """Plates Schema for the model."""

    class Meta:
        model = Plate
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    plate_number = fields.String(required=True)

