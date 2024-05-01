import unittest
import requests

class TestEndpoints(unittest.TestCase):
    def test_health_endpoint(self):
        response = requests.get('http://127.0.0.1:4004/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_mirror_endpoint(self):
        response = requests.get('http://127.0.0.1:4004/api/mirror?word=fOoBar25')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"transformed": "52RAbOoF"})

if __name__ == '__main__':
    unittest.main()

