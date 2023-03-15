from tests.conftest import test_club, test_comp

def test_book_with_valid_points_and_date(client, test_club, test_comp):

    club = test_club[0]
    comp = test_comp[2]
    date = comp['date']
    points = club['points']
    places = "1"
    response = client.post(
        '/purchasePlaces',
        data={
            'club': club['name'],
            'competition': comp['name'],
            'places': places
        }
    )
    assert response.status_code == 200
    assert b'booking complete' in response.data

    new_points = int(club['points']) - int(places)
    assert f'Points available: {new_points}' in response.data.decode()

def test_book_with_invalid_points(client, test_club, test_comp):
    club = test_club[0]
    comp = test_comp[2]
    date = comp['date']
    points = club['points']
    places = ['0', '-1', '20']
    response = client.post(
        '/purchasePlaces',
        data={
            'club': club['name'],
            'competition': comp['name'],
            'places': places
        },
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'error' in response.data

def test_book_closed_comp(client, test_club, test_comp):
    club_name = test_club[0]['name']
    comp_name = test_comp[0]['name']
    response = client.get(f'/book/{comp_name}/{club_name}')
    assert response.status_code == 200
    assert b'This competition is over' in response.data

def test_login_logout(client, test_club):
    club = test_club[0]
    club_email = club['email']
    response = client.post('/showSummary', data={"email": club_email})
    assert response.status_code == 200
    assert f"Welcome, {club_email}" in response.data.decode()
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data

def test_display_points_with_login(client, test_club):
    club_email = test_club[0]['email']
    response = client.post('/showSummary', data={"email": club_email})
    assert response.status_code == 200
    response = client.get('/displayPoints')
    assert response.status_code == 200
    assert b"Number of Points" in response.data