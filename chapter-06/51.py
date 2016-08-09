# -*- coding: utf-8 

import re

# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

# テキストファイル読み込み
file = open("nlp_50.txt", "r")
for sentence in file:
	# 文章の終わり
	sentence = re.sub("[\.;:\?\!]\n", "\n", sentence)
	# 空白で区切る
	word_list = sentence.split(" ")
	print "\n".join(word_list)