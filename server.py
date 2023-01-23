import json
from flask import Flask,render_template,request,redirect,flash,url_for

from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

def sort_competitions_date(comps):
    past = []
    present = []

    for comp in comps:
        if datetime.strptime(comp['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            past.append(comp)
        elif datetime.strptime(comp['date'], '%Y-%m-%d %H:%M:%S') >= datetime.now():
            present.append(comp)

    return past, present

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
past_competitions, present_competitions = sort_competitions_date(competitions)
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',
                                club=club,
                                past_competitions=past_competitions,
                                present_competitions=present_competitions)
    except IndexError:
        flash('Invalid email error')
        return redirect(url_for('index'))

@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        if foundCompetition in past_competitions:
            flash("This competition is over.", 'error')
            return render_template('welcome.html',
                                    club=foundClub,
                                    past_competitions=past_competitions,
                                    present_competitions=present_competitions)

        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html',
                                club=foundClub,
                                past_competitions=past_competitions,
                                present_competitions=present_competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    if (placesRequired < 1 
        or placesRequired > 12
        or placesRequired > int(club['points'])
        or placesRequired > int(competition['numberOfPlaces'])):
        flash("Wrong places number error")
        return render_template('welcome.html',
                        club=club,
                        past_competitions=past_competitions,
                        present_competitions=present_competitions)
    elif competition in past_competitions:
        flash("Can't purchase in past competition")
        return render_template('welcome.html',
                                club=club,
                                past_competitions=past_competitions,
                                present_competitions=present_competitions)
    else:
        club['points'] = int(club['points']) - placesRequired
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html',
                                club=club,
                                past_competitions=past_competitions,
                                present_competitions=present_competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))