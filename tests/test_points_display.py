import server
from server import app


def test_points_display(mocker):
    clubs = [{
        "name": "test_club",
        "points": "10",
    }]
    mocker.patch('server.clubs', clubs)

    client = app.test_client()
    response = client.get(
        "/points",
    )

    assert response.status_code == 200
    assert b"test_club" in response.data
    assert b"10" in response.data
