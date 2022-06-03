import re

import sqlalchemy
from flask import make_response, jsonify, request
from flask_restful import Resource, reqparse

from app.extensions import db
from app.model.plate import Plate
from app.model.schema import PlateSchema


class PlatesView(Resource):
    """This is the view for plates."""

    @staticmethod
    def extract_digits(plate):
        final_digit = ''
        list_of_numbers = re.findall(r'\d+', plate)

        for num in list_of_numbers:
            final_digit += num
        return final_digit

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('plate', type=str, required=True)
        args = parser.parse_args()

        plate = str(args['plate'])

        if len(plate.split("-")[0]) > 3:
            message = {
                'message': 'Sorry invalid number plate, 1 to 3 characters before the hyphen.'
            }
            return make_response(jsonify(message), 422)

        if len(plate.split("-")[1]) < 2:
            message = {
                'message': 'Sorry invalid number plate, minimum of 1 or 2 characters.'
            }
            return make_response(jsonify(message), 422)

        if len(self.extract_digits(plate.split("-")[1])) > 4:
            message = {
                'message': 'Sorry invalid number plate, maximum only 4 numbers after the hyphne.'
            }
            return make_response(jsonify(message), 422)

        if self.extract_digits(plate.split("-")[1])[0] == "0":
            message = {
                'message': 'Sorry invalid number plate, digits after hyphen cannot start with zero.'
            }
            return make_response(jsonify(message), 422)

        try:
            add_plate = Plate(plate_number=plate)
            db.session.add(add_plate)
            db.session.commit()

            message = {
                'message': 'The plate number has been successfully added.'
            }
        except sqlalchemy.exc.IntegrityError:
            message = {
                'message': 'Sorry this number plate already exists.'
            }
            return make_response(jsonify(message), 400)

        return make_response(jsonify(message), 201)

    def get(self):
        plates = Plate.query.all()
        plate_schema = PlateSchema(many=True)
        dump_data = plate_schema.dump(plates)
        return jsonify(dump_data)


class PlateSearchView(Resource):
    """Plate searching view."""

    def get(self):
        args = dict(request.args)
        plates = Plate.query.filter_by(plate_number=args.get('key')).all()
        plate_schema = PlateSchema(many=True)
        dump_data = plate_schema.dump(plates)
        return make_response(jsonify({args.get('key'): dump_data}), 200)
