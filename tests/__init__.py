import json
from unittest import TestCase

from sqlalchemy.testing import db

from app.app import application
from app.config.config import app_config


class BaseTestCase(TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        db.create_all()
        application.config.from_object(app_config["testing"])
        return application

    def setUp(self):
        self.client = application.test_client(self)

    def tearDown(self):
        """
        Drop the database
        """
        # db.drop_all()

    def add_plate_number(self, plate):
        """
         Submit tour plate number
        """
        return self.client.post(
            '/api/v1/plate',
            data=json.dumps(dict(plate=plate,)),
            content_type='application/json',)
