import os
import numpy as np
import pandas as pd


def read_ratings(user_num):
    src_file_path = os.path.dirname(os.getcwd()) + os.path.sep + 'src'
    data = pd.read_csv(src_file_path + os.path.sep + 'ratings.csv')

    items_num = 10000
    dataMat = np.zeros((user_num, items_num))

    for line in data.itertuples():
        if line[1] > user_num:
            break
        if line[2] > items_num:
            continue
        dataMat[line[1] - 1, line[2] - 1] = line[3]

    return np.mat(dataMat)
