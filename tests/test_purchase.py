import server
from server import app


def test_purchase_success(mocker):
    clubs = [{"name": "test_club"}]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "15",
    }]
    mocker.patch('server.competitions', competitions)

    client = app.test_client()
    response = client.post(
        "/purchasePlaces",
        data=dict(
            competition="test_competition",
            club="test_club",
            places="10",
        )
    )

    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data


def test_purchase_too_much(mocker):
    clubs = [{"name": "test_club"}]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "15",
    }]
    mocker.patch('server.competitions', competitions)

    client = app.test_client()
    response = client.post(
        "/purchasePlaces",
        data=dict(
            competition="test_competition",
            club="test_club",
            places="18",
        )
    )

    assert response.status_code == 200
    assert b'Purchase error' in response.data
