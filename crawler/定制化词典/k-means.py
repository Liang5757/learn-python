from gensim.models import word2vec
from sklearn.cluster import KMeans
import gensim

# 对.sava保存的模型的加载：
model = gensim.models.Word2Vec.load("word_embedding_128.word2vec")

# 获取model里面的所有关键词
keys = model.wv.vocab.keys()

# 获取词对于的词向量
wordvector = []
for key in keys:
    wordvector.append(model.wv.__getitem__(key))

# 分类
classCount = 10  # 分类数
clf = KMeans(n_clusters=classCount)
s = clf.fit(wordvector)

# 获取到所有词向量所属类别
labels = clf.labels_

# 把是一类的放入到一个字典里
classCollects = {}
for i in range(len(keys)):
    if labels[i] in classCollects.keys():
        classCollects[labels[i]].append(list(keys)[i])
    else:
        classCollects[labels[i]] = [list(keys)[i]]

for i in range(classCount):
    print('{}类：'.format(i), classCollects[i])
