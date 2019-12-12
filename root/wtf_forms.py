from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Length


class PlayerForm(FlaskForm):
    player_username = StringField('Id', validators=[DataRequired()])
    balance = FloatField('Balance', validators=[DataRequired()])
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
    player_username = StringField('Player username', validators=[DataRequired()])
    sold_time = StringField('Time of money selling', validators=[DataRequired()])
    sold_coins = FloatField('Amount of coins', validators=[DataRequired()])
    Submit = SubmitField("Create")


class CountryForm(FlaskForm):
    country_name = StringField('Name', validators=[DataRequired(), Length(3, 10, "The name should be from 3 to 10 symbols")])
    country_capital = StringField('Capital', validators=[DataRequired()])
    country_population = IntegerField('Population', validators=[DataRequired()])
    country_square = FloatField('Square', validators=[DataRequired()])
    Submit = SubmitField("Create")

    def validate(self):
        if float(self.country_population.data) < 0:
            raise ValidationError("Population more than 0")
            return False
        return True
