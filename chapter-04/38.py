# -*- coding: utf-8 -*-

import numpy as np
import pickle
from collections import Counter
from pylab import *
import matplotlib.pyplot as plt


# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描く
# 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型

# 形態素解析結果読み込み（オブジェクトをでシリアライズ）
with open('neko.txt.mecab.pickle', 'r') as f:
	book = pickle.load(f)

# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描く
word_list = []
for sentence in book:
	for morpheme in sentence:
		word_list.append(morpheme['surface'])

# 出現頻度が高い順に並べる
count = Counter(word_list)
word_frequency_count = []
for word, cnt in count.most_common():
	word_frequency_count.append(cnt)

count = Counter(word_frequency_count)
print count

x = []
# y = []
for frequency, count in count.items():
	x.append(count)
	# y.append(cnt)

# # ヒストグラム描画
plt.hist(x)
plt.title("Histgram")
plt.xlabel(u"出現頻度")
plt.ylabel(u"単語の種類")
plt.show()


