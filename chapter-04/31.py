# -*- coding: utf-8 -*-

import json
import re
import codecs
import pickle

# 動詞の表層形をすべて抽出
# 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型

# 形態素解析結果読み込み（オブジェクトをでシリアライズ）
with open('neko.txt.mecab.pickle', 'r') as f:
	book = pickle.load(f)

# print book

for sentence in book:
	for morpheme in sentence:
		if morpheme['pos'] == '動詞':
			print morpheme['surface']

