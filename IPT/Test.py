import unittest
import warnings
from api import app
from base64 import b64encode


class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    warnings.simplefilter("ignore", category=DeprecationWarning)


def test_index_page(self):
    hdr = {"Authorization": "Basic " + b64encode(b"zhar:2564").decode()}
    response = self.app.get("/", headers=hdr)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data.decode(), "<p>Hello, World!</p>")


def test_get_actors(self):
    hdr = {"Authorization": "Basic " + b64encode(b"zhar:2564").decode()}
    response = self.app.get("/tables/actors", headers=hdr)
    self.assertEqual(response.status_code, 200)
    self.assertTrue("PENELOPE" in response.data.decode())


def test_get_actor_by_id(self):
    hdr = {"Authorization": "Basic " + b64encode(b"zhar:2564").decode()}
    response = self.app.get("/tables/actors/88", headers=hdr)
    self.assertEqual(response.status_code, 200)
    self.assertTrue("PESCI" in response.data.decode())

    if name == "main":
        unittest.main()
