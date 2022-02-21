# %matplotlib notebook 启动交互式图形
# %matplotlib inline 启动静态图形

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# 设置绘图样式
plt.style.use('classic')

x = np.linspace(1, 10, 100)

# plt.plot(x, np.cos(x))
# plt.plot(x, np.sin(x))
#
# # 保存图片到本地
# plt.savefig('my_figure.png')

# from IPython.display import Image
# 保存图片到本地
# Image('my_figure.png')

# Matlib风格接口
# 这种接口是有状态的，它会持续跟踪当前图形和坐标轴
# plt.gcf()(获得当前图形), plt.gca()(获取当前坐标轴)
# 创建两个子图中的第一个
plt.subplot(2, 1, 1)    # (行, 列, 子图编号)
plt.plot(x, np.sin(x))

# 创建两个子图中的第二个
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

# 面向对象接口
# 创建图形网格
# ax是一个包含两个Axes对象的数组
fig, ax = plt.subplots(2)

# 在每个对象上调用plot()方法
ax[0].plot(x, np.cos(x))
ax[1].plot(x, np.sin(x))

# 一个会话只能使用一次plt.show()
plt.show()
