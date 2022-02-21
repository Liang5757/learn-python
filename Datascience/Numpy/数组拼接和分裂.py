import numpy as np

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [99, 99, 99]

# concatenate()以数组元组或数组列表作为第一个参数
print("左右体位：\n", np.concatenate([x, y, z]))

grid = np.array([[1, 2, 3],
                [4, 5, 6]])

# 二维数组沿第一个轴拼接
print("上下体位：\n", np.concatenate([grid, grid]))
# 二维数组沿第二个轴拼接
print("左右体位：\n", np.concatenate([grid, grid], axis=1))

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                [6, 5, 4]])
y = np.array([[9, 8, 7, 99],
              [6, 5, 4, 99]])

# 垂直栈数组
print("上下体位：\n", np.vstack([x, grid]))
# 水平栈数组
print("左右体位：\n", np.hstack([grid, y]))

x = [1, 2, 3, 99, 99, 3, 2, 1]

# 数组的分裂
x1, x2, x3 = np.split(x, [3, 5])        # 列表记录的是分裂点的位置
print("哇哦，分开啦：\n", x1, x2, x3)

grid = np.arange(16).reshape((4, 4))
print("想起你原来模样：\n", grid)
# 上下分裂
upper, lower = np.vsplit(grid, [2])     # 列表记录是分裂行的位置
print("上下体位：\n", upper, '\n', lower)
# 左右分裂
left, right = np.hsplit(grid, [2])      # 列表记录是分裂列的位置
print("左右体位：\n", left, '\n', right)
# dsplit()沿第三个维度分裂
