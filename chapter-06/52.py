# -*- coding: utf-8 

from nltk import stem
import re

# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
# Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

# テキストファイル読み込み
file = open("nlp_51.txt", "r")
for line in file:
	line = line.strip()
	# Porterのステミングアルゴリズムを適用
	stemmer = stem.PorterStemmer()
	print "{0}\t{1}".format(line, stemmer.stem(line))
