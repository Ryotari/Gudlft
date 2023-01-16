def test_book_with_valid_points(client):

    club = "Iron Temple"
    competition = "Spring Festival"
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
    competition = "Spring Festival"
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
