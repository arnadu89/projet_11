import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


def load_clubs():
    with open("clubs.json") as c:
        list_of_clubs = json.load(c)["clubs"]
        return list_of_clubs


def load_competitions():
    with open("competitions.json") as comps:
        list_of_competitions = json.load(comps)["competitions"]
        return list_of_competitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = load_competitions()
clubs = load_clubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def show_summary():
    try:
        club = [club for club in clubs if club["email"] == request.form["email"]][0]
    except IndexError as e:
        flash("Error : invalid login email")
        return redirect(url_for("index"))

    return render_template(
        "welcome.html",
        club=club,
        competitions=competitions
    )


@app.route("/book/<competition>/<club>")
def book(competition, club):
    found_club = [c for c in clubs if c["name"] == club]
    found_competition = [c for c in competitions if c["name"] == competition]
    if found_club and found_competition:
        return render_template(
            "booking.html",
            club=found_club[0],
            competition=found_competition[0]
        )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions
        )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():
    competition = [
        c for c in competitions if c["name"] == request.form["competition"]
    ][0]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    places_required = int(request.form["places"])
    competition_datetime = datetime.strptime(competition["date"], '%Y-%m-%d %H:%M:%S')
    if competition_datetime < datetime.now():
        flash("Purchase error : You can't purchase places on an outdated competition.")
    elif places_required > 12:
        flash("Purchase error : You can't purchase more than 12 places on a competition.")
    elif places_required > int(competition["numberOfPlaces"]):
        flash(f"Purchase error : You require {places_required} "
              f"places for the competition but only {competition['numberOfPlaces']} left.")
    elif places_required > int(club["points"]):
        flash(f"Purchase error : You require {places_required} "
              f"but you have only {club['points']} points.")
    else:
        competition["numberOfPlaces"] = str(int(competition["numberOfPlaces"]) - places_required)
        club["points"] = str(int(club["points"]) - places_required)
        flash("Great-booking complete!")
    return render_template(
        "welcome.html",
        club=club,
        competitions=competitions
    )


@app.route("/points")
def display_clubs_points():
    return render_template(
        "clubs_points.html",
        clubs=clubs
    )


@app.route("/logout")
def logout():
    return redirect(url_for("index"))


@app.template_filter()
def date_over(competition_date_string):
    competition_date = datetime.strptime(competition_date_string, "%Y-%m-%d %H:%M:%S")
    return competition_date > datetime.now()
