from tests import BaseTestCase


class TestsTours(BaseTestCase):

    def test_plate_submission_successfully(self):
        """Tests when submitting """

        response = self.add_plate_number("M-PP193")
        print(" r ", response.data)
        self.assertEqual(response.status_code, 201)
