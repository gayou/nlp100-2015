# -*- coding: utf-8 -*-

import pickle
from collections import Counter

# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べる
# 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型

# 形態素解析結果読み込み（オブジェクトをでシリアライズ）
with open('neko.txt.mecab.pickle', 'r') as f:
	book = pickle.load(f)

# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べる
word_list = []
for sentence in book:
	for morpheme in sentence:
		word_list.append(morpheme['surface'])

# 出現頻度が高い順に並べる
count = Counter(word_list)
for word, cnt in count.most_common():
	print word, cnt
