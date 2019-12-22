import math
import operator

data1 = [([1, 1, 2], "A"),
         ([1, 2, 1], "A"),
         ([2, 2, 1], "A"),
         ([5, 5, 5], "B")]

data_to_classify1 = [{'player_username': 'p1', 'data': [5, 5, 4]},
                     {'player_username': 'p2', 'data': [0, 0, 3]},
                     {'player_username': 'p3', 'data': [1, 2, 1]}]


def start_pnn(data, data_to_classify):
    sigma = 0.1

    def pdf(weights, value_to_classify):
        temp = sum([weight * x for x, weight in zip(weights, value_to_classify)])
        return math.e ** ((temp - 1) / sigma ** 2)

    def normalize(array):
        length = math.sqrt(sum([value ** 2 for value in array]))
        return [value / length for value in array]

    def classify(samples, point):
        normalized_samples = [(normalize(sample[0]), sample[1]) for sample in samples]
        normalized_point = normalize(point)

        summation = {}
        for normalized_data_sample in normalized_samples:
            sample_pdf_value = pdf(normalized_data_sample[0], normalized_point)
            summation[normalized_data_sample[1]] = summation.get(normalized_data_sample[1], 0) + sample_pdf_value

        return max(summation.items(), key=operator.itemgetter(1))[0]

    result = []
    for to_classify in data_to_classify:
        classi = classify(data, to_classify['data'])
        player_id = to_classify['player_username']
        result.append({player_id: classi})
    return result


# res = start_pnn(data1, data_to_classify1)
# print(res)
