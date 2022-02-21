import numpy as np

# 将1到9放入3*3矩阵中
grid = np.arange(1, 10).reshape((3, 3))
print(grid)
# 若进行此构建，必须满足原始数组大小与变形后数组的大小一致

x = np.array([1, 2, 3])
# 通过变形获得列向量
reshape_x = x.reshape((3, 1))
print("列向量：\n", reshape_x)
# 通过newaxis获得列向量
newaxis_x = x[np.newaxis, :]
print("行向量：\n", newaxis_x)
