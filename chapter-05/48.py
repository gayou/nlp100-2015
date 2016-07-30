# -*- coding: utf-8 -*-

from cabocha_parser import CabochaParser
import sys


# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

# 各文節は（表層形の）形態素列で表現する
# パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
# 「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

# 吾輩は -> 見た
# ここで -> 始めて -> 人間という -> ものを -> 見た
# 人間という -> ものを -> 見た
# ものを -> 見た

filename = "neko.txt.cabocha"

parser = CabochaParser()
parser.parse(filename)

cnt = 0
book = parser.getBook()
for sentence in book:
	chunk_pass_list = []

	for chunk in sentence:
		# print chunk
		# 文節パスツリーのリストに含まれるか？
		for i, chunk_pass in enumerate(chunk_pass_list):
			if chunk.chunk_id == chunk_pass[-1].dst:
				chunk_pass_list[i].append(chunk)

		# 名詞を含む文節か
		noun = chunk.getPart("名詞")
		if noun != None:
			chunk_pass_list.append([chunk])


	for chunk_pass in chunk_pass_list:
		print " -> ".join([chunk.getText() for chunk in chunk_pass])
