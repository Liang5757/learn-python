import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# plt.figure()实例可以被看做能够容纳各种坐标轴、图形、文字和标签的容器
fig = plt.figure()
# 创建坐标轴ax
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))

# 调整图形：线条的颜色与风格
plt.plot(x, np.sin(x - 0), color='blue')            # 标准颜色名称
plt.plot(x, np.sin(x - 1), color='g')               # 缩写颜色代码
plt.plot(x, np.sin(x - 2), color='0.75')            # 范围在0~1的灰度值
plt.plot(x, np.sin(x - 3), color='#FFDD44')         # 十六进制(RRGGBB，00~FF)
plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))   # RGB元组，范围在0~1
plt.plot(x, np.sin(x - 5), color='chartreuse')      # HTML颜色名称

# 用linestyle参数调整线条风格
# linestyle='-'代表实线、'--'代表虚线、'-.'代表点划线、':'代表实点线
# 还可以和在一起'-g'、'--c'、'-.k'、':r'

plt.plot(x, np.sin(x))
# plt.xlim()调整x轴坐标上限
plt.xlim(-1, 11)
# plt.ylim()调整y轴坐标上限
plt.ylim(-1.5, 1.5)
# 逆序设置坐标轴可以转置

plt.show()
