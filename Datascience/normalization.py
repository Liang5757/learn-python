import numpy as np


# 线性归一化
def autoNorm(dataSet):
    # 每列的最小值
    minVals = dataSet.min(0)
    # 每列的最大值
    maxVals = dataSet.max(0)
    # 每列最小值和最大值的差值
    ranges = maxVals - minVals
    # 用以储存归一化数据
    normDataSet = np.zeros(np.shape(dataSet))
    # dataSet的行数
    m = dataSet.shape[0]
    # oldvalue - min
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    # (oldvalue - min) / (max - min)
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    # 返回归一化数据集、差值范围、每列的的最小值
    return normDataSet, ranges, minVals


# 方差均值归一化
def zScoreNorm(dataSet):
    return (dataSet - np.mean(dataSet)) / np.std(dataSet)
