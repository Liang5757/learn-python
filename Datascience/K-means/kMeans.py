import numpy as np
import matplotlib.pyplot as plt
import time


# 读取文件
def loadDataSet(filename):
    # 用以储存数据
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        # 去掉首尾空格后,按制表符分割每行,返回列表
        curLine = line.strip().split(',')
        # 提取前两个数据存储
        fltLine = list(map(float, curLine[0: 2]))
        # 添加到数据列表中
        dataMat.append(fltLine)
    return np.mat(dataMat)


# 计算欧式距离
def distEclud(vecA, vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))


# 构建随机簇质心
def randCent(dataSet, k):
    # 获取矩阵第二维的长度
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        # 确保在整个数据集的范围内
        minJ = min(dataSet[:, j])
        # 每列最大值和最小值的差值
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)
    return centroids


# k-means均值聚类算法
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    # 获得列表的第一维长度
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m, 2)))
    # createCent找到k给随机中心点
    centroids = createCent(dataSet, k)
    # 用以判断簇质心是否不变
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf  # float类型的最大值
            # 簇别号
            minIndex = -1
            for j in range(k):
                # 样本点到簇质心的距离
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    # 当前的最小距离
                    minDist = distJI
                    # 当前最小值属于哪一簇
                    minIndex = j
            # 判断簇质心是否改变
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            # 将当前点的类别号和最小距离赋值给clusterAssment的一行
            clusterAssment[i, :] = minIndex, minDist ** 2
        # print(centroids)
        for cent in range(k):
            # nonzero返回非0元素和零元素的索引元组
            # 依次获得同一簇的样本
            ptsinClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = np.mean(ptsinClust, axis=0)
        # 返回各个簇质心、[每个点的类别号，到该簇质心的距离平方]
        return centroids, clusterAssment


# 绘制图形
def draw(dataSet):
    # 设置画布大小，避免图像间重叠
    plt.figure(figsize=(16, 12))
    for k in range(2, 6):
        # k-means聚类
        # start = time.time()
        centroids, clusterAssment = kMeans(dataSet, k)
        # end = time.time()
        # print("time:", end - start)
        plt.subplot(2, 2, k-1)
        # 绘制随机簇质心，颜色为红色，并显示图形标题，点大小为30
        plt.scatter(np.array(centroids[:, 0]), np.array(centroids[:, 1]), label='centroids', c='red', s=30)
        # 绘制数据集图形,颜色依类别改变，点大小为20
        plt.scatter(np.array(dataSet[:, 0]), np.array(dataSet[:, 1]), c=10+np.array(clusterAssment[:, 0]), s=20)
        plt.title('k={}'.format(k))
        plt.xlabel('sepal length/cm')
        plt.ylabel('sepal width/cm')
    # 保存图片
    plt.savefig('K_means.png')
    plt.legend()
    plt.show()


# 运行函数
def Kmean_main():
    # 读取文件
    dataSet = loadDataSet('iris.data')
    # 画出图像
    draw(dataSet)


if __name__ == '__main__':
    Kmean_main()
