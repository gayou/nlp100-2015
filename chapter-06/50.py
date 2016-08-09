# -*- coding: utf-8 

import re

# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

# テキストファイル読み込み
file = open("nlp.txt", "r")
for line in file:
	# 文の区切りパターンを探す
	pause_list = re.findall("[\.;:\?\!][\s]+[A-Z]", line)

	# 文の区切りパターンがない場合、そのまま出力
	if len(pause_list) == 0:
		print line
		continue

	# 文の区切りパターンがある場合
	idx = 0
	for pause in pause_list:
		result = re.search(pause, line, re.DOTALL)
		span = result.span()
		print line[idx:span[0] + 1]
		idx = span[1] - 1
