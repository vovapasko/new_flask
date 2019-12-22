from root.ai.pnn import start_pnn
from root.ai.tools import get_data, convert_format

experienced_player_data = get_data('experienced.txt')
inexperienced_player_data = get_data('inexperienced.txt')

exp_converted = convert_format(experienced_player_data, 'experienced')
inexp_converted = convert_format(inexperienced_player_data, 'inexperienced')
sum = exp_converted + inexp_converted

classify_data = [{'player_username': 'player1', 'data': [1200, 24000, 4500, 12000]},
                 {'player_username': 'player2', 'data': [10200, 4000, 5400, 8000]}]

res = start_pnn(sum, classify_data)
print(res)
