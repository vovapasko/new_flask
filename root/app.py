import json

import flask
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect
import os
import plotly
import plotly.graph_objs as go

from root.db import Database
from root.entities import Player, Bet, Bank
from root.wtf_forms import PlayerForm, BetForm, BankForm

app = Flask(__name__)
SECRET_KEY = os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgres://abxvkvvzwysgdj:144d9b0117f3f20d098dad0fcfbb2180b0827e043c6d7e0375bf15ea9f6afcef@ec2-174-129-205-197.compute-1.amazonaws.com:5432/d72ivr9hbohppk"
database = Database()


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    with database:
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
    with database:
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
    with database:
        all_players = database.fetchAllPlayers()
        return render_template("players.html", all_players=all_players)


@app.route('/players/update/<player_username>', methods=["GET", "POST"])
def update_player(player_username):
    with database:
        player_data = database.fetchPlayer(player_username)
        form = PlayerForm(player_username=player_data.player_username,
                          balance=player_data.balance,
                          passwrd=player_data.passwrd)
    if request.method == "POST":
        balance = form.balance.data
        passwrd = form.passwrd.data
        with database:
            database.updatePlayer(player_username, balance, passwrd)
        return redirect(url_for("players"))

    return render_template("update_player.html", form=form)


@app.route('/players/delete_player/<player_username>')
def delete_player(player_username):
    with database:
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
            with database:
                database.createPlayer(player)
            return redirect(url_for("players"))
    return render_template("create_player.html", form=form)


@app.route('/bets')
def bets():
    with database:
        all_bets = database.fetchAllBets()
        return render_template("bet.html", all_bets=all_bets)


@app.route('/bets/<bet_id>', methods=["GET", "POST"])
def update_bet(bet_id):
    with database:
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
        with database:
            database.updateBet(bet_id, bet_money, won_money, won_bet, bet_time)
        return redirect(url_for("bets"))
    return render_template("update_bet.html", form=form)


@app.route('/bets/delete_bet/<bet_id>')
def delete_bet(bet_id):
    with database:
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
            with database:
                database.createBet(bet)
            return redirect(url_for("bets"))
    return render_template("create_bet.html", form=form)


@app.route('/banks')
def banks():
    with database:
        all_banks = database.fetchAllBanks()
        return render_template("bank.html", all_banks=all_banks)


@app.route('/banks/<player_username>/<sold_time>', methods=["GET", "POST"])
def update_bank(player_username, sold_time):
    with database:
        bank_data = database.fetchBank(player_username, sold_time)
        form = BankForm(
            player_username=bank_data.player_username,
            sold_time=bank_data.sold_time,
            sold_coins=bank_data.sold_coins
        )
    if request.method == "POST":
        sold_coins = form.sold_coins.data
        with database:
            database.updateBank(player_username, sold_time, sold_coins)
        return redirect(url_for("banks"))
    return render_template("update_bank.html", form=form)


@app.route('/banks/delete_bank/<player_username>/<sold_time>')
def delete_bank(player_username, sold_time):
    with database:
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
            with database:
                database.createBank(bank)
            return redirect(url_for("banks"))
    return render_template("create_bank.html", form=form)


@app.route('/casinos')
def casinos():
    player_bets = {}
    players_list = []
    with database:
        all_casinos = database.fetchAllCasinos()
        for casino in all_casinos:
            player_bets['player_username'] = casino.player_username
            bet = database.fetchBet(casino.bet_id)
            player_bets['bet'] = bet
            players_list.append(player_bets)
            player_bets = {}
        return render_template("casinos.html", player_bets=players_list)


if __name__ == '__main__':
    app.run(debug=True)
