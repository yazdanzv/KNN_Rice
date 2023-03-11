import math

import numpy as np

from Normalize import *

new_data = [15231, 525.5789795, 229.7498779, 85.09378815, 0.928882003, 15617, 0.572895527]  # Random Data
K = 23  # Random Number


def add_new_data(_new_data: list):  # Checked
    data, data_tr = read()
    data = list(data)
    data.append(new_data)
    data = np.array(data)
    data_tr = data.transpose()
    return data, data_tr


def normalize_new_data(_data_tr):  # Checked
    means = get_mean(_data_tr)
    standard_deviations = get_standard_deviation(_data_tr)
    norm_new_data = normalize(_data_tr, means, standard_deviations)
    return norm_new_data


def key_sort(item):
    return item[0]


def calculate_distance(_list_tr):  # Checked
    distances = []
    _list = _list_tr.transpose()
    new_data_norm = _list[-1]
    # print(len(_list))
    # print(_list[0])
    # print(_list[-1])
    for i in range(len(_list)):
        dis = 0
        for j in range(len(_list[i])):
            dis += math.pow((new_data_norm[j] - _list[i][j]), 2)
        dis = math.sqrt(dis)
        distances.append(dis)
    classes = read_class()
    classes = list(classes)
    for i in range(len(classes)):
        classes[i] = list(classes[i])
    distances.pop()
    for i in range(len(distances)):
        distances[i] = [distances[i], classes[i][0]]
    list.sort(distances, key=key_sort)
    return distances


def knn(_distances):
    answers = []
    for i in range(K):
        answers.append(_distances[i])
    count_cammeo = 0
    count_osmancik = 0
    for i in range(len(answers)):
        if answers[i][1] == 'Cammeo':
            count_cammeo += 1
        if answers[i][1] == 'Osmancik':
            count_osmancik += 1
    print(answers)
    print(count_cammeo)
    print(count_osmancik)
    if count_cammeo > count_osmancik:
        return "Class : Cammeo"
    elif count_cammeo < count_osmancik:
        return "Class : Osmancik"
    else:
        return "Class : it could be both of them !!!"


def start():
    data, data_tr = add_new_data(new_data)
    norm = normalize_new_data(data_tr)
    norm = np.array(norm)
    distances = calculate_distance(norm)
    print(knn(distances))


start()


