import pytest

from server import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client

"""@pytest.fixture()
def fixture():
    clubs =
    {"clubs":[
    {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    },
    {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    },
    {   "name":"She Lifts",
        "email": "kate@shelifts.co.uk",
        "points":"12"
    }"""