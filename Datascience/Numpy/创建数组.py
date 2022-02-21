import numpy as np

# NumPy的数组是固定类型的，有利于高效的储存和操作数据

# 如果类型不匹配，numpy会向上转换（如果可行）
a1 = np.array([3.14, 1, 2])
print(a1)
# dtype:明确设置数组类型
a2 = np.array([1, 2, 3, 4, 5], dtype='float32')
print(a2)
# 初始化多维数组
a3 = np.array([range(i, i + 3) for i in [2, 4, 5]])
print(a3)

# mat()函数将数组转化为矩阵(matrix)
randMat = np.mat(np.random.rand(4, 4))
print(randMat)
# 矩阵求逆
invRandMat = randMat.I
print(invRandMat)
# 矩阵乘法
myEye = randMat * invRandMat        # 矩阵*矩阵的逆为同阶单位矩阵
print(myEye)
# eye()函数创建单位矩阵
Eye = np.eye(4)
print(myEye - Eye)      # 输出误差
