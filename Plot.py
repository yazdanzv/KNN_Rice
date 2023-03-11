import numpy as np

from Normalize import *
import matplotlib.pyplot as plt
import random

print("Select Which Freature Do You Want To See : ")
print("(Number 0 to 7)")
n = int(input())
FEATURE_NUMBER = n
print("Enter 1 For Data Sample And 2 for Norm Data Sample")
mode = int(input())
# Process Starts
data, data_tr = read()
norm = normalize(data_tr, get_mean(data_tr), get_standard_deviation(data_tr))
data_sample = np.random.choice(data_tr[FEATURE_NUMBER], 10, replace=False)
sample_index = []
for i in range(len(data_sample)):
    index = np.where(data_tr[FEATURE_NUMBER] == data_sample[i])
    sample_index.append(index[0][0])
norm = np.array(norm)
norm_sample = []
for i in range(len(sample_index)):
    norm_sample.append(norm[FEATURE_NUMBER][sample_index[i]])
norm_sample = np.array(norm_sample)


def show_norm_sample():
    plt.hist(norm_sample)
    plt.title('Norm Sample Data')
    plt.show()


def show_sample():
    plt.hist(data_sample)
    plt.title('Sample Data')
    plt.show()


if mode == 1:
    show_sample()
elif mode == 2:
    show_norm_sample()
else:
    raise Exception('No Such Option!!!')
