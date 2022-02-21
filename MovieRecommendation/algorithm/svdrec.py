from utils.sim import *
from utils.read_file import *
import time

# 用来计算在给定相似度计算方法的条件下，用户对物品的估计评分值
# dataMat:数据集, user:用户, simMeas:相似度测量方法, item:待测物品的列数
def standEst(dataMat, user, simMeas, item):
    # 物品的个数
    n = np.shape(dataMat)[1]
    # 初始化评分值
    simTotal = 0.0
    ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user, j]
        # 如果用户对该物品的打分为0则跳过
        if userRating == 0:
            continue
        # overLap为两个物品中均已被评分元素的行数
        overLap = np.nonzero(np.logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0))[0]
        # 若没有均被评分的元素，则相似度为0
        if len(overLap) == 0:
            similarity = 0
        # 否则基于均被评分的元素计算相似度
        else:
            similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])
        # 计算相似度总和
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal

# 获取去除噪声数据后的Sigma仅留的个数
def sigmaNum(Sigma, percentage):
    # 对对角矩阵求和
    Sigma_sum = np.sum(Sigma)
    # 能量和
    energy_sum = 0
    # 保留的Sigma数
    k = 0
    for i in Sigma:
        energy_sum += i
        k += 1
        if energy_sum >= Sigma_sum * percentage:
            return k


# 基于SVD的评分估计
# dataMat:数据集, user:用户, simMeas:相似度测量方法, item:待测物品的列数
def svdEst(dataMat, user, simMeas, item):
    # 物品的个数
    n = np.shape(dataMat)[1]
    # 初始化评分值
    simTotal = 0.0
    ratSimTotal = 0.0
    U, Sigma, VT = la.svd(dataMat)
    k = sigmaNum(Sigma, 0.9)
    # 构建对角矩阵
    Sig4 = np.mat(np.eye(k) * Sigma[:k])
    xformedItems = dataMat.T * U[:, :k] * Sig4.I
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item:
            continue
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        # 计算相似度总和
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal

# 推荐引擎：产生最高的N个推荐结果
# dataMat:数据集, user:用户, N:需要推荐的个数,simMeas:相似度测量方法, item:待测物品的列数
def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    # 所有未被评分物品的列数
    unratedItems = np.nonzero(dataMat[user, :].A == 0)[1]
    # 若均以评分则放回
    if len(unratedItems) == 0:
        return 'you rated everything'
    # 用以储存(索引, 预测评分)
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    # 逆序排序预测评分,返回前N个
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[: N]


myMat = read_ratings(100)
movie_recommend = recommend(myMat, 2, estMethod=standEst)
print(movie_recommend)