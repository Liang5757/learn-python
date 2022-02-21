调用的库：
import numpy as np
import operator
import matplotlib.pyplot as plt
import pandas as pd

”“”
    @name : file2matrix
    @param ：filename(文件名)
    @description : 读取文件
    @return : 返回数据集(数组)，对应的类别(列表)
“””
def file2matrix(filename)

”“”
    @name : autoNorm
    @param ：dataSet(数据集)
    @description : 线性归一化
    @return : 归一化数据集(数组)、差值范围、每列的的最小值
“””
def autoNorm(dataSet)

”“”
    @name : classify0
    @param ：inX(待测数据), dataSet(训练集), labels(训练集的类别), k(临近的个数)
    @description : KNN算法
    @return : 返回数目最大的类别
“””
def classify0(inX, dataSet, labels, k)

”“”
    @name : datingClassTest
    @param ：k(临近的个数)
    @description : 分类测试，输出错误率
    @return : 无
“””
def datingClassTest(k)

”“”
    @name : nominal2int
    @param ：datingLabels(数据集的类别)
    @description : 将标称型数据修改为数值型数据
    @return : 数值型数据(数组)
“””
def nominal2int(datingLabels)

”“”
    @name : draw
    @param ：无
    @description : 画出原散点图
    @return : 无
“””
def draw()