import server
import pytest


def test_load_clubs():
    clubs = server.load_clubs()

    assert clubs[0]["name"] == "Simply Lift"


def test_load_competitions():
    competitions = server.load_competitions()

    assert competitions[0]["name"] == "Spring Festival"
