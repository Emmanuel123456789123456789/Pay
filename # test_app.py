# test_app.py
import unittest
import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome to China Bank!')

if __name__ == '__main__':
    unittest.main()
