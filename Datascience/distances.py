import numpy as np


# 欧式距离
def distEclud(vecA, vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))


# 曼哈顿距离
def distManh(vecA, vecB):
    return np.sum(np.abs(vecA - vecB))


# 切比雪夫距离
def distCheby(vecA, vecB):
    return np.abs(vecA - vecB).max


# 余弦相似度
def distCos(vecA, vecB):
    return np.dot(vecA, vecB) / np.sqrt(np.sum(vecA ** 2)) / np.sqrt(np.sum(vecB ** 2))

