# -*- coding: utf-8 -*-

import json
import re
import codecs
import pickle

# 2つの名詞が「の」で連結されている名詞句を抽出
# 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型

# 形態素解析結果読み込み（オブジェクトをでシリアライズ）
with open('neko.txt.mecab.pickle', 'r') as f:
	book = pickle.load(f)

# print book

noun_phrase = []
for sentence in book:
	for morpheme in sentence:
		if len(noun_phrase) == 0 and morpheme['pos'] == '名詞':
			noun_phrase.append(morpheme['surface'])
			
		elif len(noun_phrase) == 1:
			if morpheme['surface'] == "の":
				noun_phrase.append(morpheme['surface'])
			else:
				noun_phrase = []

		elif len(noun_phrase) == 2:
			if morpheme['pos'] == '名詞':
				noun_phrase.append(morpheme['surface'])
				print "".join(noun_phrase)
				noun_phrase = []
			else:
				noun_phrase = []

