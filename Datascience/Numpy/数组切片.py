import numpy as np

x = np.array(np.random.randint(10, size=(3, 4)))

# 原始数组
print(x)
# 获取第一列
print("第一行:\n", x[:, 0])
# 取两行三列
print("两行三列:\n", x[:2, :3])
# 三行，每隔一列
print("三行，每隔一列:\n", x[:3, ::2])
# 转置数组
print("reverse:\n", x[::-1, ::-1])

# 列切片若为空可省略
# Numpy数组的切片是数组数据的视图
# 而python列表的切片是值的副本

# 优点：在处理非常大的数据集时，可以获取或处理这些数据集的片段，而不用复制底层的数据存缓

# 仍可以通过copy()实现复制数组或子数组
x_sub_copy = x[:2, :2].copy()
print("二行二列的复制：\n", x_sub_copy)
