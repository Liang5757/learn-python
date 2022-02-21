import numpy as np

# 奇异值分解中Sigma是对角矩阵
# 但这里Sigma是以大到小依次排列的一维数组，是为了节省空间
U, Sigma, VT = np.linalg.svd([[1, 1], [7, 7]])

