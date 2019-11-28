from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import TIMESTAMP

Base = declarative_base()


class Player(Base):
    __tablename__ = "player"
    player_id = Column(Integer, primary_key=True)
    balance = Column(Integer, nullable=False)
    passwrd = Column(String(64), nullable=False)


class Bank(Base):
    __tablename__ = "bank"
    player_id = Column(Integer, ForeignKey(Player.player_id), primary_key=True)
    sold_time = Column(TIMESTAMP, primary_key=True)
    sold_coins = Column(Float, nullable=False)


class Bet(Base):
    __tablename__ = "bet"
    bet_id = Column(Integer, primary_key=True)
    bet_money = Column(Float, nullable=False)
    won_money = Column(Float, nullable=False)
    won_bet = Column(Boolean, nullable=False)
    bet_time = Column(TIMESTAMP, nullable=False)


class Usernames(Base):
    __tablename__ = "usernames"
    player_id = Column(Integer, ForeignKey(Player.player_id), primary_key=True)
    player_name = Column(String(64))
    play_surname = Column(String(64))
    player_nickname = Column(String(64), nullable=False)


class Casino(Base):
    __tablename__ = "casino"
    player_id = Column(Integer, ForeignKey(Player.player_id), primary_key=True)
    bet_id = Column(Integer, ForeignKey(Bet.bet_id), primary_key=True)
