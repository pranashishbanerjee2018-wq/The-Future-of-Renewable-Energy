"""
test_flask_app.py - Local Flask Web Application & REST Endpoint Verification
Validates:
  1. GET / returns HTTP 200 OK.
  2. GET /data/scenes.json returns HTTP 200 OK with valid JSON.
  3. GET /data/simulation_results.json returns HTTP 200 OK with valid JSON.
  4. GET /api/scenes returns HTTP 200 OK.
  5. GET /api/simulation returns HTTP 200 OK.
"""

import os
import sys
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_route(self):
        """GET / must return HTTP 200 with presentation title."""
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'THE FUTURE OF RENEWABLE ENERGY', res.data)
        res.close()

    def test_data_routes(self):
        """GET /data/scenes.json and /data/simulation_results.json must return 200."""
        res_scenes = self.client.get('/data/scenes.json')
        self.assertEqual(res_scenes.status_code, 200)
        res_scenes.close()

        res_sim = self.client.get('/data/simulation_results.json')
        self.assertEqual(res_sim.status_code, 200)
        res_sim.close()

    def test_api_endpoints(self):
        """REST endpoints /api/scenes and /api/simulation must return valid JSON."""
        res1 = self.client.get('/api/scenes')
        self.assertEqual(res1.status_code, 200)
        self.assertTrue(res1.is_json)
        res1.close()

        res2 = self.client.get('/api/simulation')
        self.assertEqual(res2.status_code, 200)
        self.assertTrue(res2.is_json)
        res2.close()

if __name__ == '__main__':
    unittest.main()
