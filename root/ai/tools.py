def get_data(filename):
    str_data = open(filename, 'r').read()
    lines = str_data.split('\n')
    del lines[-1]
    return_data = []
    for line in lines:
        tmp = line.split(',')
        return_data.append([float(tmp[0]), float(tmp[1]), float(tmp[2]), float(tmp[3])])
    return return_data


def convert_format(data, name):
    converted = []
    for datum in data:
        converted.append((datum, name))
    return converted
