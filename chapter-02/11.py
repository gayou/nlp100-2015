# -*- coding: utf-8 -*-

# ファイル読み込み
for line in open("hightemp.txt"):
	# タブをスペースに置換
	print line.replace("\t", " ")

