import server


def test_integration():
    client = server.app.test_client()

    # Testing loadClubs
    assert server.clubs[0]["name"] == "Simply Lift"

    # Testing loadCompetitions
    assert server.competitions[0]["name"] == "Spring Festival"

    # Testing index
    index_response = client.get("/")
    assert index_response.status_code == 200

    # Testing showSummary
    showsummary_response = client.post(
        "/showSummary",
        data=dict(
            email="john@simplylift.co"
        )
    )

    assert showsummary_response.status_code == 200

    # Testing book
    book_response = client.get(
        f"/book/{server.competitions[0]['name']}/{server.clubs[0]['name']}"
    )

    assert book_response.status_code == 200

    # Testing puchasePlaces
    purchase_response = client.post(
        "/purchasePlaces",
        data=dict(
            competition=server.competitions[0]["name"],
            club=server.clubs[0]["name"],
            places="5",
        )
    )

    assert purchase_response.status_code == 200

    # Testing logout
    logout_response = client.get("/logout")

    assert logout_response.status_code == 302
