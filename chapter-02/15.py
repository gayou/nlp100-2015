# -*- coding: utf-8 -*-

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち最後のN行だけを表示

import codecs
import sys

# print "py.14"
# print sys.argv
# print len(sys.argv)
# print "-----"

# 引数確認
if len(sys.argv) != 2 or sys.argv[1].isdigit() == False:
	print "ERR:コマンドの第1引数に自然数を入力してください"
	exit()

# 引数取得
lines = int(sys.argv[1])

# ファイル読み込み
file = codecs.open("hightemp.txt", "r", "utf-8").readlines()
for i in range(len(file) - lines, len(file)):
	print file[i]
