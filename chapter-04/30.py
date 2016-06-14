# -*- coding: utf-8 -*-

import json
import re
import codecs
import pickle

# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装する
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現する
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

# 形態素解析結果読み込み
book = []
sentence = []
for line in codecs.open("neko.txt.mecab", "r"):
	# 一文の終わりの場合
	if line.strip() == 'EOS':
		book.append(sentence)
		sentence = []
		continue

	# 文の開始または途中の場合
	column = re.split("[\t|,]", line)
	morpheme = {
		'surface': column[0],
		'base'   : column[7],
		'pos'    : column[1],
		'pos1'   : column[2]
	}
	sentence.append(morpheme)
	print morpheme
	# break

print book


#️ オブジェクトをシリアライズしてファイルにキャッシュする
with open('neko.txt.mecab.pickle', 'wb') as f:
	pickle.dump(book, f)

