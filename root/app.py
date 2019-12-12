import json

import flask
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect
import os
import plotly
import plotly.graph_objs as go

from root.db import Database
from root.entities import Player, Bet, Bank, Country
from root.wtf_forms import PlayerForm, BetForm, BankForm, CountryForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgres://abxvkvvzwysgdj:144d9b0117f3f20d098dad0fcfbb2180b0827e043c6d7e0375bf15ea9f6afcef@ec2-174-129-205-197.compute-1.amazonaws.com:5432/d72ivr9hbohppk"
database = Database()


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    player_data = database.fetchAllPlayers()
    player_username = []
    balance = []
    for player in player_data:
        player_username.append(player.player_username)
        balance.append(player.balance)
    bar = go.Bar(
        x=player_username,
        y=balance
    )
    bet_data = database.fetchAllBets()
    bet_id = []
    bet_money = []
    for bet in bet_data:
        bet_id.append(bet.bet_id)
        bet_money.append(bet.bet_money)
    pie = go.Pie(
        labels=bet_id,
        values=bet_money
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("dashboard.html", graphsJSON=graphsJSON)


@app.route('/players')
def players():
    all_players = database.fetchAllPlayers()
    return render_template("players.html", all_players=all_players)


@app.route('/players/update/<player_username>', methods=["GET", "POST"])
def update_player(player_username):
    player_data = database.fetchPlayer(player_username)
    form = PlayerForm(player_username=player_data.player_username,
                      balance=player_data.balance,
                      passwrd=player_data.passwrd)
    if request.method == "POST":
        balance = form.balance.data
        passwrd = form.passwrd.data
        database.updatePlayer(player_username, balance, passwrd)
        return redirect(url_for("players"))

    return render_template("update_player.html", form=form)


@app.route('/players/delete_player/<player_username>')
def delete_player(player_username):
    database.deletePlayer(player_username)
    return redirect(url_for("players"))


@app.route('/players/new_player', methods=["GET", "POST"])
def create_player():
    form = PlayerForm()
    if request.method == "POST":
        if not form.validate():
            return render_template("create_player.html", form=form)
        else:
            username = form.player_username.data
            balance = form.balance.data
            passwrd = form.passwrd.data
            player = Player(player_username=username, balance=balance, passwrd=passwrd)
            database.createPlayer(player)
            return redirect(url_for("players"))
    return render_template("create_player.html", form=form)


@app.route('/bets')
def bets():
    all_bets = database.fetchAllBets()
    return render_template("bet.html", all_bets=all_bets)


@app.route('/bets/<bet_id>', methods=["GET", "POST"])
def update_bet(bet_id):
    bet_data = database.fetchBet(bet_id)
    form = BetForm(
        bet_id=bet_data.bet_id,
        bet_money=bet_data.bet_money,
        won_money=bet_data.won_money,
        won_bet=bet_data.won_bet,
        bet_time=bet_data.bet_time
    )
    if request.method == "POST":
        bet_money = form.bet_money.data
        won_money = form.won_money.data
        won_bet = form.won_bet.data
        bet_time = form.bet_time.data
        database.updateBet(bet_id, bet_money, won_money, won_bet, bet_time)
        return redirect(url_for("bets"))
    return render_template("update_bet.html", form=form)


@app.route('/bets/delete_bet/<bet_id>')
def delete_bet(bet_id):
    database.deleteBet(bet_id)
    return redirect(url_for("bets"))


@app.route('/bets/new_bet', methods=["GET", "POST"])
def create_bet():
    form = BetForm()
    if request.method == "POST":
        if not form.validate():
            return render_template("create_bet.html", form=form)
        else:
            id = form.bet_id.data
            bet_money = form.bet_money.data
            won_money = form.won_money.data
            won_bet = form.won_bet.data
            bet_time = form.bet_time.data.format('%Y-%m-%d %H:%M:%S')
            bet = Bet(bet_id=id, bet_money=bet_money, won_money=won_money,
                      won_bet=won_bet, bet_time=bet_time)
            database.createBet(bet)
            return redirect(url_for("bets"))
    return render_template("create_bet.html", form=form)


@app.route('/banks')
def banks():
    all_banks = database.fetchAllBanks()
    return render_template("bank.html", all_banks=all_banks)


@app.route('/banks/<player_username>/<sold_time>', methods=["GET", "POST"])
def update_bank(player_username, sold_time):
    bank_data = database.fetchBank(player_username, sold_time)
    form = BankForm(
        player_username=bank_data.player_username,
        sold_time=bank_data.sold_time,
        sold_coins=bank_data.sold_coins
    )
    if request.method == "POST":
        sold_coins = form.sold_coins.data
        database.updateBank(player_username, sold_time, sold_coins)
        return redirect(url_for("banks"))
    return render_template("update_bank.html", form=form)


@app.route('/banks/delete_bank/<player_username>/<sold_time>')
def delete_bank(player_username, sold_time):
    database.deleteBank(player_username, sold_time)
    return redirect(url_for("banks"))


@app.route('/banks/new_bank', methods=["GET", "POST"])
def create_bank():
    form = BankForm()
    if request.method == "POST":
        if not form.validate():
            return render_template("create_bank.html", form=form)
        else:
            username = form.player_username.data
            sold_time = form.sold_time.data.format('%Y-%m-%d %H:%M:%S')
            sold_coins = form.sold_coins.data
            bank = Bank(player_username=username, sold_coins=sold_coins, sold_time=sold_time)
            database.createBank(bank)
            return redirect(url_for("banks"))
    return render_template("create_bank.html", form=form)


@app.route('/shop')
def shop():
    all_countries = database.fetchAllCountries()
    return render_template("countries.html", all_countries=all_countries)


@app.route('/countries/new_country', methods=["GET", "POST"])
def create_country():
    form = CountryForm()
    if request.method == "POST":
        if not form.validate():
            return render_template("create_country.html", form=form)
        else:
            name = form.country_name.data
            capital = form.country_capital.data
            population = form.country_population.data
            square = form.country_square.data
            new_country = Country(country_name=name, country_capital=capital,
                                  country_population=population, country_square=square)
            database.createCountry(new_country)
            return redirect(url_for("shop"))
    return render_template("create_country.html", form=form)


@app.route('/get', methods=["GET"])
def create_country_hardcode():
    new_counrty = Country(country_name="New Germany", country_capital="New Berlin",
                          country_population=100, country_square=10.5)
    database.createCountry(new_counrty)
    return "Country created succesfully"


@app.route('/bar')
def country_bar():
    country_data = database.fetchAllCountries()
    name_country = []
    population = []
    for country in country_data:
        name_country.append(country.country_name)
        population.append(country.country_population)
    bar = go.Bar(
        x=name_country,
        y=population
    )

    data = {
        "bar": [bar],
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("bar.html", graphsJSON=graphsJSON)


@app.route('/casinos')
def casinos():
    all_casinos = database.fetchAllCasinos()
    return render_template("casinos.html", all_casinos=all_casinos)


if __name__ == '__main__':
    app.run(debug=True)
