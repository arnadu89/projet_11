import server
from server import app


def test_index_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_login_fail():
    client = app.test_client()
    response = client.post(
        "/showSummary",
        data=dict(
            email="wrong_email@fail.test"
        ),
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Error : invalid login email' in response.data


def test_login_success(mocker):
    clubs = [{"email": "valid_email@success.test"}]
    mocker.patch('server.clubs', clubs)

    client = app.test_client()
    response = client.post(
        "/showSummary",
        data=dict(
            email="valid_email@success.test"
        )
    )

    assert response.status_code == 200
