import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import credentials
from entities import Player, Bet, Bank, Casino, Usernames


class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    cstr = 'postgresql://{user}:{password}@{hostname}/{database}'.format(
        user=credentials.username,
        password=credentials.password,
        hostname=credentials.host,
        database=credentials.database
    )
    engine = db.create_engine(cstr)

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    # Player

    def createPlayer(self, player):
        session = Session(bind=self.connection)
        session.add(player)
        session.commit()
        print("Player created successfully!")

    def updatePlayer(self, player_id, player_balance, player_passwd):
        session = Session(bind=self.connection)
        dataToUpdate = {Player.balance: player_balance, Player.passwrd: player_passwd}
        playerData = session.query(Player).filter(Player.player_id == player_id)
        playerData.update(dataToUpdate)
        session.commit()
        print("Player updated successfully!")

    def fetchAllPlayers(self):
        self.session = Session(bind=self.connection)
        players = self.session.query(Player).all()
        return players

    def fetchPlayer(self, player_id):
        self.session = Session(bind=self.connection)
        player = self.session.query(Player).filter(Player.player_id == player_id).first()
        return player

    def deletePlayer(self, player_id):
        session = Session(bind=self.connection)
        playerData = session.query(Player).filter(Player.player_id == player_id).first()
        session.delete(playerData)
        session.commit()
        print("Player deleted successfully!")

    # username
    def delete_username(self, player_id):
        session = Session(bind=self.connection)
        playerData = session.query(Usernames).filter(Usernames.player_id == player_id).first()
        session.delete(playerData)
        session.commit()

    # Bet

    def createBet(self, bet):
        session = Session(bind=self.connection)
        session.add(bet)
        session.commit()
        print("Bet created successfully!")

    def updateBet(self, bet_id, bet_money, won_money, won_bet, bet_time):
        session = Session(bind=self.connection)
        dataToUpdate = {Bet.bet_money: bet_money, Bet.won_money: won_money,
                        Bet.won_bet: won_bet, Bet.bet_time: bet_time}
        betData = session.query(Bet).filter(Bet.bet_id == bet_id)
        betData.update(dataToUpdate)
        session.commit()
        print("Bet updated successfully!")

    def fetchAllBets(self):
        self.session = Session(bind=self.connection)
        bets = self.session.query(Bet).all()
        return bets

    def fetchBet(self, bet_id):
        self.session = Session(bind=self.connection)
        bet = self.session.query(Bet).filter(Bet.bet_id == bet_id).first()
        return bet

    def deleteBet(self, bet_id):
        session = Session(bind=self.connection)
        betData = session.query(Bet).filter(Bet.bet_id == bet_id).first()
        session.delete(betData)
        session.commit()
        print("Bet deleted successfully!")

    # Bank

    def createBank(self, bank):
        session = Session(bind=self.connection)
        session.add(bank)
        session.commit()
        print("Bank created successfully!")

    def updateBank(self, player_id, sold_time, sold_coins):
        session = Session(bind=self.connection)
        dataToUpdate = {Bank.sold_time: sold_time, Bank.sold_coins: sold_coins}
        betData = session.query(Bank).filter(Bank.player_id == player_id)
        betData.update(dataToUpdate)
        session.commit()
        print("Bank updated successfully!")

    def updateBankWithTime(self, player_id, sold_time, sold_coins):
        session = Session(bind=self.connection)
        dataToUpdate = {Bank.sold_coins: sold_coins}
        bankData = session.query(Bank).filter(Bank.player_id == player_id).filter(Bank.sold_time == sold_time)
        bankData.update(dataToUpdate)
        session.commit()
        print("Bank updated successfully!")

    def fetchAllBanks(self):
        self.session = Session(bind=self.connection)
        banks = self.session.query(Bank).all()
        return banks

    def fetchBank(self, player_id, sold_time):
        self.session = Session(bind=self.connection)
        bank = self.session.query(Bank).filter(Bank.player_id == player_id).filter(Bank.sold_time == sold_time).first()
        return bank

    def deleteBank(self, player_id, sold_time):
        session = Session(bind=self.connection)
        bankData = session.query(Bank).filter(Bank.player_id == player_id).filter(
            Bank.sold_time == sold_time).filter().first()
        session.delete(bankData)
        session.commit()
        print("Bank deleted successfully!")
