# -*- coding: utf-8 -*-

# ファイル読み込み
lineCount = 0
for line in open("hightemp.txt"):
	lineCount += 1

print "行数:" + str(lineCount)