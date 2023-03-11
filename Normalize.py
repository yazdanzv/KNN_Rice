import pandas as pd
import numpy as np
import statistics

PATH = 'E:\\DataMining\\Rice_Cammeo_Osmancik.xlsx'


def read_class():  # Checked
    df = pd.read_excel(PATH, usecols=[7])
    _classes = np.array(df.values.tolist())
    return _classes


def read():  # Checked
    df = pd.read_excel(PATH, usecols=[0, 1, 2, 3, 4, 5, 6])
    _list = np.array(df.values.tolist()).astype(float)  # for getting the rpws
    _list_tr = _list.transpose().astype(float)  # for getting the columns
    return _list, _list_tr


def get_mean(_list: list):  # Checked
    _means = []
    for i in range(len(_list)):
        _means.append(statistics.mean(_list[i]))
    return _means


def get_standard_deviation(_list: list):  # Checked
    _standard_deviations = []
    for i in range(len(_list)):
        _standard_deviations.append(statistics.stdev(_list[i]))
    return _standard_deviations


def normalize(_list: list, _means: list, _standard_deviations: list):  # Checked
    _norm_df = []
    for i in range(len(_list)):
        temp = []
        for j in range(len(_list[i])):
            new_data = (_list[i][j] - _means[i]) / _standard_deviations[i]
            temp.append(new_data)
        _norm_df.append(temp)
    return _norm_df


def start():  # Checked
    # Reading Xlsx File
    df_list, df_list_tr = read()
    # Getting Mean and Standard Deviation
    means = get_mean(df_list_tr)
    standard_deviation = get_standard_deviation(df_list_tr)
    # Normalizing
    norm_df = normalize(df_list_tr, means, standard_deviation)
    # norm_df = np.array(norm_df)
    return norm_df