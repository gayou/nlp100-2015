# -*- coding: utf-8 -*-

import numpy as np
import pickle
from collections import Counter
from pylab import *
import matplotlib.pyplot as plt


# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロット

# 形態素解析結果読み込み（オブジェクトをでシリアライズ）
with open('neko.txt.mecab.pickle', 'r') as f:
	book = pickle.load(f)

# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロット
word_list = []
for sentence in book:
	for morpheme in sentence:
		word_list.append(morpheme['surface'])

# 出現頻度が高い順に並べる
count = Counter(word_list)
word_frequency_count = []
for word, cnt in count.most_common():
	word_frequency_count.append(cnt)
	# print word, cnt

# 両対数グラフ描画
x = np.array(range(1, len(count) + 1))
y = np.array(word_frequency_count)
# print len(x), len(y)

plt.xscale("log")
plt.yscale("log")
plt.title(u"出現頻度と順位の相関性")
plt.xlabel(u"順位(log)")
plt.ylabel(u"出現頻度(log)")

# plt.plot(x, word_frequency_count)
plt.scatter(x, word_frequency_count)
plt.show()


