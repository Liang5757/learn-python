import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import numpy as np

# x = np.linspace(0, 100, 10000)
# plt.plot(x, np.sin(x), '--b', label='sin(x)')
# plt.xlim(-100, 100)
# plt.ylim(-1.5, 1.5)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('sin(x)')

# plt.legend()
#
# rng = np.random.RandomState(0)
# for maker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
#     plt.plot(rng.rand(5), rng.rand(5), maker, label="marker='{0}'".format(maker))
#     plt.legend(numpoints=1)
#     plt.xlim(0, 1.8)

x = np.linspace(0, 10, 30)
y = np.sin(x)

# plt.plot(x, y, '-p', color='gray',
#          makersize=15, linewidth=4,
#          makerfacecolor='white',
#          makeredgecolor='gray',
#          makeredgewidth=2)
# plt.ylim(-1.2, 1.2)

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = rng.rand(100) * 1000
# alpha参数来调整透明度
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
# 显示颜色条
plt.colorbar()

plt.show()
