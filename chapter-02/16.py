# -*- coding: utf-8 -*-

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割

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

# 作成するファイル数
cnt_file = (len(file) / lines + 1) if (len(file) % lines > 0) else (len(file) / lines)

# ファイル分割
for i in range(cnt_file):
 	filename = "hightemp_split_" + str(i) + ".txt"
 	fh = codecs.open(filename, "w", "utf-8")
 	for j in range(lines):
 		fh.write(file[i * lines + j])

 	fh.close()
