# -*- coding: utf-8 -*-

# 1列目の文字列の種類（異なる文字列の集合）を求める

import codecs
import sys

# ファイル読み込み
s = set()
for line in codecs.open("hightemp.txt", "r", "utf-8"):
	line = line[:-1].split()
	# print line[0]
	s.add(line[0])

# セットを出力
# print s
for str in s:
	print str

