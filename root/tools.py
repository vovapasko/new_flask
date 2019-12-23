from root.db import Database
from root.ai.run_ai import run


def get_data():
    database = Database()
    player_data = []
    with database:
        players = database.fetchAllPlayers()
        for player in players:
            username = player.player_username
            player_dict = {'player_username': username, 'balance': player.balance}
            banks = database.fetchBankUsername(username)
            sum_sold_coins = 0
            for bank in banks:
                sum_sold_coins += bank.sold_coins
            player_dict['sold_coins'] = sum_sold_coins
            bets = database.fetchAllCasinoPlayerBets(username)
            bet_money_sum = 0
            bet_loss_sum = 0
            for bet in bets:
                pure_bet = database.fetchBet(bet.bet_id)
                bet_money_sum += pure_bet.bet_money
                if pure_bet.won_money < 0:
                    bet_loss_sum += pure_bet.won_money
            player_dict['bet_money'] = bet_money_sum
            player_dict['bet_loss'] = bet_loss_sum
            player_data.append(player_dict)
    return player_data


def handle_for_ai_data(dict_player_data):
    player_usernames = []
    player_data = []
    for player in dict_player_data:
        player_usernames.append(player['player_username'])
        player_data.append([player['balance'], player['sold_coins'],
                            player['bet_money'], player['bet_loss']])
    return {'usernames': player_usernames,
            'data': player_data}


data = get_data()
handled = handle_for_ai_data(data)
res = run(handled['usernames'], handled['data'])
print(res)
