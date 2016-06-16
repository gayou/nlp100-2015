# -*- coding: utf-8 -*-

import pickle

# 名詞の連接（連続して出現する名詞）を最長一致で抽出
# 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型

# 形態素解析結果読み込み（オブジェクトをでシリアライズ）
with open('neko.txt.mecab.pickle', 'r') as f:
	book = pickle.load(f)

# 名詞の連接（連続して出現する名詞）を最長一致で抽出
noun_phrases = []
for sentence in book:
	noun_phrases = []
	for morpheme in sentence:
		if morpheme['pos'] == '名詞':
			noun_phrases.append(morpheme['surface'])
		else:
			if len(noun_phrases) >= 2:
				print "".join(noun_phrases)

			noun_phrases = []

