调用的库：
import numpy as np
import matplotlib.pyplot as plt

”“”
    @name : loadDataSet
    @param ：filename(文件名)
    @description : 读取文件
    @return : 数据集(矩阵)
“””
def loadDataSet(filename)

”“”
    @name : distEclud
    @param ：vecA(数组), vecB(数组)
    @description : 计算欧式距离
    @return : 两两点间距离
“””
def distEclud(vecA, vecB)

”“”
    @name : randCent
    @param ：dataSet(数据集), k(生成k个簇质心)
    @description : 构建随机簇质心
    @return : 簇质心(数组)
“””
def randCent(dataSet, k)

”“”
    @name : kMeans
    @param ：dataSet(数据集), k(簇质心的个数),distMeas(距离公式), createCent(随机簇质心生成方法)
    @description : K-means算法
    @return : 各个簇质心、[每个点的类别号，到该簇质心的距离平方]
“””
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent)

”“”
    @name : draw
    @param ：dataSet(数据集)
    @description : 绘制图形
    @return : 无
“””
def draw(dataSet)