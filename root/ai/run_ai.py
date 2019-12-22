from root.ai.pnn import start_pnn
from root.ai.tools import get_data, convert_format


def run(usernames, data):
    experienced_player_data = get_data('experienced.txt')
    inexperienced_player_data = get_data('inexperienced.txt')

    exp_converted = convert_format(experienced_player_data, 'experienced')
    inexp_converted = convert_format(inexperienced_player_data, 'inexperienced')
    sum = exp_converted + inexp_converted
    classify_data = []
    for i in range(len(usernames)):
        tmp = {'player_username': usernames[i], 'data': data[i]}
        classify_data.append(tmp)
    res = start_pnn(sum, classify_data)
    return res


# test_usernames = ['player1', 'player2']
# test_data = [[1200, 24000, 4500, 12000], [10200, 4000, 5400, 8000]]
# res = run(test_usernames, test_data)
# print(res)