import server
from server import app


def test_booking_page_success(mocker):
    clubs = [{
        "name": "test_club",
        "points": "20",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2023-10-22 13:30:00",
        "numberOfPlaces": "15",
    }]
    mocker.patch('server.competitions', competitions)

    route_url = f"/book/{competitions[0]['name']}/{clubs[0]['name']}"

    client = app.test_client()
    response = client.get(
        route_url
    )

    assert response.status_code == 200
    assert b'Places available' in response.data


def test_booking_page_club_fail(mocker):
    clubs = [{
        "name": "test_club",
        "points": "20",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2023-10-22 13:30:00",
        "numberOfPlaces": "15",
    }]
    mocker.patch('server.competitions', competitions)

    route_url = f"/book/{competitions[0]['name']}/fail_club_name"

    client = app.test_client()
    response = client.get(
        route_url
    )

    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data


def test_booking_page_competition_fail(mocker):
    clubs = [{
        "name": "test_club",
        "points": "20",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2023-10-22 13:30:00",
        "numberOfPlaces": "15",
    }]
    mocker.patch('server.competitions', competitions)

    route_url = f"/book/fail_competition_name/{clubs[0]['name']}"

    client = app.test_client()
    response = client.get(
        route_url
    )

    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data


def test_purchase_success(mocker):
    clubs = [{
        "name": "test_club",
        "points": "20",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2023-10-22 13:30:00",
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
    assert clubs[0]["points"] == "10"
    assert competitions[0]["numberOfPlaces"] == "5"


def test_purchase_more_than_available(mocker):
    clubs = [{
        "name": "test_club",
        "points": "10",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2023-10-22 13:30:00",
        "numberOfPlaces": "8",
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
    assert b'Purchase error' in response.data


def test_purchase_more_than_12(mocker):
    clubs = [{
        "name": "test_club",
        "points": "10",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2023-10-22 13:30:00",
        "numberOfPlaces": "18",
    }]
    mocker.patch('server.competitions', competitions)

    client = app.test_client()
    response = client.post(
        "/purchasePlaces",
        data=dict(
            competition="test_competition",
            club="test_club",
            places="15",
        )
    )

    assert response.status_code == 200
    assert b"Purchase error" in response.data


def test_purchase_more_than_club_points(mocker):
    clubs = [{
        "name": "test_club",
        "points": "10",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "2023-10-22 13:30:00",
        "numberOfPlaces": "18",
    }]
    mocker.patch('server.competitions', competitions)

    client = app.test_client()
    response = client.post(
        "/purchasePlaces",
        data=dict(
            competition="test_competition",
            club="test_club",
            places="15",
        )
    )

    assert response.status_code == 200
    assert b"Purchase error" in response.data


def test_purchase_outdated_competition(mocker):
    clubs = [{
        "name": "test_club",
        "points": "10",
    }]
    mocker.patch('server.clubs', clubs)

    competitions = [{
        "name": "test_competition",
        "date": "1910-10-22 13:30:00",
        "numberOfPlaces": "18",
    }]
    mocker.patch('server.competitions', competitions)

    client = app.test_client()
    response = client.post(
        "/purchasePlaces",
        data=dict(
            competition="test_competition",
            club="test_club",
            places="5",
        )
    )

    assert response.status_code == 200
    assert b"Purchase error" in response.data
