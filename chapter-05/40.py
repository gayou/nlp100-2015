# -*- coding: utf-8 -*-

from morph import Morph
import codecs
import re


# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
# さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

book = []
sentence = []

for line in codecs.open("neko.txt.cabocha", "r"):
	# 
	if line[0] == '*':
		continue

	# 一文の終わりの場合
	if line.strip() == 'EOS':
		if len(sentence) > 0:
			book.append(sentence)
			sentence = []
		continue

	# 文の開始または途中の場合
	column = re.split("[\t|,]", line)
	morpheme = Morph(column[0], column[7], column[1], column[2])
	sentence.append(morpheme)
	# print morpheme

# print book
print book[2]