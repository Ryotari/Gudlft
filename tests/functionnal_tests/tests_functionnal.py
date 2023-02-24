def test_book_with_valid_points_and_date(client):

    club = "Iron Temple"
    competition = "Future Competition"
    date = "2024-01-18 10:00:00"
    points = "4"
    places = "1"
    response = client.post(
        '/purchasePlaces',
        data={
            'club': club,
            'competition': competition,
            'places': places
        }
    )
    assert response.status_code == 200
    assert b'booking complete' in response.data

    new_points = int(points) - int(places)
    test_message = f'Points available: {new_points}'
    test_message = bytes(test_message, 'utf-8')
    assert test_message in response.data

def test_book_with_invalid_points(client):
    club = "Iron Temple"
    competition = "Future Competition"
    date = "2024-01-18 10:00:00"
    points = "4"
    places = ['0', '-1', '20']
    response = client.post(
        '/purchasePlaces',
        data={
            'club': club,
            'competition': competition,
            'places': places
        },
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'error' in response.data

def test_book_with_invalid_date(client):

    club = "Iron Temple"
    competition = "Spring Festival"
    date = "2020-01-18 10:00:00"
    points = "4"
    places = "1"
    response = client.get(f'/book/{competition}/{club}')
    assert response.status_code == 200
    assert b"This competition is over." in response.data

def test_login_logout(client):
    response = client.post('/showSummary', data={"email": "admin@irontemple.com"})
    assert response.status_code == 200
    assert b"Welcome, admin@irontemple.com" in response.data
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data