# -*- coding: utf-8 -*-

# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示

import codecs
import sys
from collections import Counter

# ファイル読み込み
print u"ファイル内容"
count = {}
word_list = []
for line in codecs.open("hightemp.txt", "r", "utf-8"):
	print line[:-1]
	line = line[:-1].split()
	word = line[0]
	count[word] = count.get(word, 0) + 1
	word_list.append(word)

# print count
print ""


# 1カラム目の単語の出現頻度を表示
list = []
for word in count:
	list.append([str(count[word]), word])


# 1列目の要素で降順にソートして出現頻度を表示
list.sort(key=lambda x:(x[0]), reverse=True)
print u"出現頻度"
for line in list:
	print "\t".join(line)

print ""

# Counterを使って出現頻度を表示
count = Counter(word_list)
for word, cnt in count.most_common():
	print cnt, word
