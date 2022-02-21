import numpy as np
import operator
import matplotlib.pyplot as plt
import pandas as pd
import time

# 读取文件
def file2matrix(filename):
    fr = open(filename)
    # 读取每一行作为列表的元素返回
    arrayOLines = fr.readlines()
    # 数据个数
    numberOfLines = len(arrayOLines)
    # 储存数据的数组
    returnMat = np.zeros((numberOfLines, 2))
    # 储存类别的列表
    classLabelVector = []
    for index, line in enumerate(arrayOLines):
        # 去除首尾空格,并以逗号分隔作为列表的元素返回
        listFromLine = line.strip().split(',')
        # 提取前两个数据存储
        returnMat[index, :] = list(map(float, listFromLine[0: 2]))
        # 提取最后一个数据(类别)存储
        classLabelVector.append(listFromLine[-1])
    # 返回数据，对应的类别
    return returnMat, classLabelVector


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


# 高斯函数设置权重
def gaussian(distance, sigma=10.0):
    return np.exp((-distance ** 2)/(2*sigma ** 2))


# 反函数设置权重
def inverse(distance, const=10.0):
    return 1/(distance+const)


# inX:测试数据，dataSet:训练数据集，labels:训练数据集的类别，k:临近的个数
def classify0(inX, dataSet, labels, k):
    # 训练数据集的数据数
    dataSetSize = dataSet.shape[0]
    # 当前点到所有点的坐标差值
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # 每个差值的平方
    sqDiffMat = diffMat ** 2
    # 每个数据坐标差值之和
    sqDistances = sqDiffMat.sum(axis=1)
    # 欧式距离，对每个数据坐标差值之和开方
    distances = sqDistances ** 0.5
    # 将distances中的元素从小到大排列，提取其对应的索引，赋给sortedDistIndicies
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        # 获得对应下标的类别
        voteIlabel = labels[sortedDistIndicies[i]]
        # 给相同的类别次数计数，若不存在则返回0
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # sorted按第二位逆序排序返回新list[(key, value), ...]
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    # 返回数目最大的类别
    return sortedClassCount[0][0]


# 分类测试
def datingClassTest(k):
    # 总数据数和测试集之比
    hoRatio = 0.30
    # 读取文件
    datingDataMat, datingLabels = file2matrix('iris.data')
    # 归一化特征值
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 行数
    m = normMat.shape[0]
    # 测试数据数
    numTestVecs = int(m*hoRatio)
    # 分类错误数
    errorCount = 0.0
    start = time.time()
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs: m], k)
        print("the classfier came back with: %s, the real answer is: %s" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    end = time.time()
    print("time:", (end - start)/numTestVecs)
    print("the total error rate is：%f" % (errorCount / float(numTestVecs)))


# 将标称型数据修改为数值型数据
def nominal2int(datingLabels):
    # 将类别转化为pandas对象
    df = pd.DataFrame([{'iris_type': i} for i in datingLabels])
    # 去重并为类型编号
    class_mapping = {label: idx for idx, label in enumerate(np.unique(df['iris_type']))}
    print(class_mapping)
    # 用数值编号替换df内的iris_type列
    df['iris_type'] = df['iris_type'].map(class_mapping)
    return np.array(df)


# 绘制
def draw():
    # 读取文件
    datingDataMat, datingLabels = file2matrix('iris.data')
    # 将标称型数据修改为数值型数据
    datingLabels = nominal2int(datingLabels)
    # 图形容器
    fig = plt.figure()
    # 坐标轴
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
               20.0*np.squeeze(datingLabels) + 10, 20.0*np.squeeze(datingLabels) + 10)
    plt.title('Iris')
    plt.xlabel('sepal length/cm')
    plt.ylabel('sepal width/cm')
    plt.savefig('iris.png')
    plt.show()


datingClassTest(3)
draw()
