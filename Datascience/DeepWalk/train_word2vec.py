from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# 训练模型
sentences = LineSentence('./data/deepwalk_seq.txt')
# size：词向量的维度
# window：上下文环境的窗口大小
# min_count：忽略出现次数低于min_count的词
model = Word2Vec(sentences, size=32, window=8, min_count=5, workers=4)

# 保存模型
model.save('word2vec')

print(model.wv.similarity(u'item_1655', u'item_947'))
