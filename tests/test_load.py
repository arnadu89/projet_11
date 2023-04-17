import server
import pytest


@pytest.fixture
def mocker_load_clubs(mocker):
    pass
    # clubs = [{
    #     "name": "test_name",
    #     "email": "test_email@test.email",
    #     "points": "30",
    # }]
    #
    # mocked_open_clubs = mocker.mock_open(read_data=clubs)
    # builtin_open = "builtins.open"
    # mocker.patch(builtin_open, mocked_open_clubs)


def test_load_clubs(mocker_load_clubs):
    pass
    test_club = server.load_clubs()

    # assert test_club[0]["name"] == "test_name"
