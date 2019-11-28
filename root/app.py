import flask
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect
import os

from db import Database
from entities import Player, Bet, Bank
from wtf_forms import PlayerForm, BetForm, BankForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
database = Database()


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/players')
def players():
    all_players = database.fetchAllPlayers()
    return render_template("players.html", all_players=all_players)


@app.route('/players/update/<player_id>', methods=["GET", "POST"])
def update_player(player_id):
    player_data = database.fetchPlayer(player_id)
    form = PlayerForm(id=player_data.player_id,
                      balance=player_data.balance,
                      passwrd=player_data.passwrd)
    if request.method == "POST":
        balance = form.balance.data
        passwrd = form.passwrd.data
        database.updatePlayer(player_id, balance, passwrd)
        return redirect(url_for("players"))

    return render_template("update_player.html", form=form)


@app.route('/players/delete_player/<player_id>')
def delete_player(player_id):
    database.deletePlayer(player_id)
    return redirect(url_for("players"))


@app.route('/players/new_player', methods=["GET", "POST"])
def create_player():
    form = PlayerForm()
    if request.method == "POST":
        if not form.validate():
            return render_template("create_player.html", form=form)
        else:
            id = form.id.data
            balance = form.balance.data
            passwrd = form.passwrd.data
            player = Player(player_id=id, balance=balance, passwrd=passwrd)
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


@app.route('/banks/<player_id>/<sold_time>', methods=["GET", "POST"])
def update_bank(player_id, sold_time):
    bank_data = database.fetchBank(player_id, sold_time)
    form = BankForm(
        player_id=bank_data.player_id,
        sold_time=bank_data.sold_time,
        sold_coins=bank_data.sold_coins
    )
    if request.method == "POST":
        sold_coins = form.sold_coins.data
        database.updateBank(player_id, sold_time, sold_coins)
        return redirect(url_for("banks"))
    return render_template("update_bank.html", form=form)


@app.route('/banks/delete_bank/<player_id>/<sold_time>')
def delete_bank(player_id, sold_time):
    database.deleteBank(player_id, sold_time)
    return redirect(url_for("banks"))


@app.route('/banks/new_bank', methods=["GET", "POST"])
def create_bank():
    form = BankForm()
    if request.method == "POST":
        if not form.validate():
            return render_template("create_bank.html", form=form)
        else:
            id = form.player_id.data
            sold_time = form.sold_time.data.format('%Y-%m-%d %H:%M:%S')
            sold_coins = form.sold_coins.data
            bank = Bank(player_id=id, sold_coins=sold_coins, sold_time=sold_time)
            database.createBank(bank)
            return redirect(url_for("banks"))
    return render_template("create_bank.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
