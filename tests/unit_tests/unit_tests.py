from server import loadClubs, loadCompetitions, sort_competitions_date

def test_display_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data

def test_login_with_valid_email(client):
    response = client.post('/showSummary', data={'email': "admin@irontemple.com"})
    assert response.status_code == 200
    assert b"Welcome, admin@irontemple.com" in response.data

def test_invalid_email_error(client):

    response = client.post('/showSummary', data={'email': 'test@simplylift.com'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid email error' in response.data

def test_load_clubs(client):
    list_of_clubs = loadClubs()
    assert "'name': 'Simply Lift'" in str(list_of_clubs[0])

def test_load_competitions(client):
    list_of_competitions = loadCompetitions()
    assert "'name': 'Spring Festival'" in str(list_of_competitions[0])

def test_sort_competitions(client):
    comps = loadCompetitions()
    past_competitions, present_competitions = sort_competitions_date(comps)
    assert len(past_competitions) >= 1
    assert len(present_competitions) >= 1

def test_display_points(client):
    response = client.get('/displayPoints')
    assert response.status_code == 200
    assert b"Number of Points" in response.data
