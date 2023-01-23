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
