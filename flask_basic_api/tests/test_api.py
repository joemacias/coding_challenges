import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_data_endpoint(self):
        response = self.app.get('/api/data')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Welcome to JOE API!')
    
    def test_basic_response_endpoint(self):
        response = self.app.get('/api/test')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'This is a test!!')

if __name__ == '__main__':
    unittest.main()