# 编造文本、分词
from jieba import lcut
sentences = ['吴彦祖', '张学友', '吴彦祖我', '张学友我刘德华吴彦祖',
             '苹果', '苹果香蕉', '草莓香蕉', '草莓苹果']
ls_of_words = [lcut(sentence) for sentence in sentences]

# 生成字典和词ID
from gensim.corpora import Dictionary
dt = Dictionary(ls_of_words).token2id
print(dt)
ls_of_wids = [[dt[word] for word in words] for words in ls_of_words]
print(ls_of_wids)
# 共现矩阵: 通过统计一个事先指定大小的窗口内的word共现次数，以word周边的共现词的次数做为当前word的vector
import numpy as np
dimension = len(dt)  # 维数
matrix = np.matrix([[0] * dimension] * dimension)
#增加窗口条件，也可以去掉窗口条件
def co_occurrence_matrix(ls,windows=3):
    length = len(ls)
    for i in range(length):
        left = max(0, i - windows)
        right = min(length, i + windows + 3)
        for j in range(left, right):
            if i != j:
                matrix[[ls[i]], [ls[j]]] += 1
for ls in ls_of_wids:
    co_occurrence_matrix(ls)
print(matrix)

# 奇异值分解（Singular Value Decomposition）
U, s, Vh = np.linalg.svd(matrix, full_matrices=False)

# 聚类(cluster)
X = -U[:, 0:2]
from sklearn.cluster import KMeans
labels = KMeans(n_clusters=2).fit(X).labels_
colors = ('y', 'r')

# 可视化
import matplotlib.pyplot as mp
mp.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
for word in dt.keys():
    i = dt[word]
    mp.scatter(X[i, 1], X[i, 0], c=colors[labels[i]], s=400, alpha=0.4)
    mp.text(X[i, 1], X[i, 0], word, ha='center', va='center')
mp.show()
