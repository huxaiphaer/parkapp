from tests import BaseTestCase


class TestsTours(BaseTestCase):

    def test_plate_submission_successfully(self):
        """Tests when submitting """

        response = self.add_plate_number("M-PP144")
        self.assertEqual(response.status_code, 201)

    def test_get_all_plates(self):
        """Test get all plates"""
        response = self.get_all_number_plates()
        self.assertEqual(response.status_code, 200)
