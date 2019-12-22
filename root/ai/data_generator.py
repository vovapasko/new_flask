import numpy

elements_amount = 1000
start_balance = 1000
start_sold_coins = 1000


def generate_data_experienced_player():
    end_balance = start_balance * 2000
    end_sold_coins = start_sold_coins * 10
    start_bet_sum = start_balance * 0.05
    end_bet_sum = end_balance * 0.3
    start_loss = start_balance * 0.1
    finished_loss = end_balance * 0.3
    balance_set = numpy.around(numpy.linspace(start_balance, end_balance, num=elements_amount), decimals=2)
    sold_coins_set = numpy.around(numpy.linspace(start_sold_coins, end_sold_coins, num=elements_amount), decimals=2)
    bet_set = numpy.around(numpy.linspace(start_bet_sum, end_bet_sum, num=elements_amount), decimals=2)
    loss_set = numpy.around(numpy.linspace(start_loss, finished_loss, num=elements_amount), decimals=2)
    writetoFile(balance_set, sold_coins_set, bet_set, loss_set, filename='experienced.txt')


def generate_data_inexperienced_player():
    end_balance = start_balance * 700
    end_sold_coins = start_sold_coins * 2000
    start_bet_sum = start_balance * 0.3
    end_bet_sum = end_balance * 0.7
    start_loss = start_balance * 0.3
    finished_loss = end_balance * 0.9
    balance_set = numpy.around(numpy.linspace(start_balance, end_balance, num=elements_amount), decimals=2)
    sold_coins_set = numpy.around(numpy.linspace(start_sold_coins, end_sold_coins, num=elements_amount), decimals=2)
    bet_set = numpy.around(numpy.linspace(start_bet_sum, end_bet_sum, num=elements_amount), decimals=2)
    loss_set = numpy.around(numpy.linspace(start_loss, finished_loss, num=elements_amount), decimals=2)
    writetoFile(balance_set, sold_coins_set, bet_set, loss_set, filename='inexperienced.txt')


def writetoFile(first, second, third, fourth, filename='file.txt'):
    file = open(filename, 'w')
    for i in range(elements_amount):
        str_to_write = str(first[i]) + ',' + str(second[i]) + ',' + str(third[i]) + ',' + str(
            fourth[i]) + '\n'
        file.write(str_to_write)


generate_data_experienced_player()
generate_data_inexperienced_player()