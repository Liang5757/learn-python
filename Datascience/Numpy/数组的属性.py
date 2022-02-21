import numpy as np

# 为Numpy的随机数生成器设置一组种子值，以确保每次程序执行时都可以生成同样的随机数组
np.random.seed(0)       # 设置种子

x1 = np.random.randint(10, size=6)             # 一维数组
x2 = np.random.randint(10, size=(3, 4))        # 二维数组
x3 = np.random.randint(10, size=(3, 4, 5))     # 三维数组

print("x3 ndim:", x3.ndim)      # 数组的维度
print("x3 shape:", x3.shape)    # 每个维度的大小
print("x3 size:", x3.size)      # 数组的总大小
print("x3 dtype:", x3.dtype)     # 数组的数据类型
print("x3 itemsize:", x3.itemsize, "bytes")     # 每个数组元素的字节大小
print("x3 nbytes:", x3.nbytes, "bytes")         # 数组总字节大小
