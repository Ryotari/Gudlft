import pytest
import server
from server import app

@pytest.fixture
def test_club():
    return [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13",
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4",
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12",
        }
    ]

@pytest.fixture
def test_comp():
    return [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Future Competition",
            "date": "2023-10-22 13:30:00",
            "numberOfPlaces": "15"
        }
    ]

"""@pytest.fixture
def app(mocker):
    mocker.patch.object(server, "COMPETITIONS", test_comp())
    mocker.patch.object(server, "CLUBS", test_club())
    return create_app({"TESTING": True})"""

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client
