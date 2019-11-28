from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, BooleanField
from wtforms.validators import DataRequired


class PlayerForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    balance = IntegerField('Balance', validators=[DataRequired()])
    passwrd = StringField('Password', validators=[DataRequired()])
    Submit = SubmitField("Create")


class BetForm(FlaskForm):
    bet_id = IntegerField('Id', validators=[DataRequired()])
    bet_money = FloatField('Money to bet', validators=[DataRequired()])
    won_money = FloatField('Win money', validators=[DataRequired()])
    won_bet = BooleanField('Bet won?')
    bet_time = StringField('Time of the bet', validators=[DataRequired()])
    Submit = SubmitField("Create")


class BankForm(FlaskForm):
    player_id = IntegerField('player id', validators=[DataRequired()])
    sold_time = StringField('Time of money selling', validators=[DataRequired()])
    sold_coins = FloatField('Amount of coins', validators=[DataRequired()])
    Submit = SubmitField("Create")
