# -*- coding: utf-8 -*-

# 各行を3コラム目の数値の降順にソートする

import codecs
import sys

# ファイル読み込み
print u"ソート前"
list = []
for line in codecs.open("hightemp.txt", "r", "utf-8"):
	print line[:-1]
	line = line[:-1].split()
	list.append(line)

print ""

# 3列目の要素でソート
list.sort(key=lambda x:(x[2]), reverse=True)
# print list
print u"ソート後"
for line in list:
	print "\t".join(line)

