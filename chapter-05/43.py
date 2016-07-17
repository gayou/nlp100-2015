# -*- coding: utf-8 -*-

from cabocha_parser import CabochaParser


# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

filename = "neko.txt.cabocha"

parser = CabochaParser()
parser.parse(filename)

book = parser.getBook()
for sentence in book:
	for chunk in sentence:
		# 名詞を含まない分節はスキップ
		if chunk.existsPart('名詞') == False:
			continue

		# 係り先文節が存在しない場合はスキップ
		dst = int(chunk.dst)
		if dst == -1:
			continue

		# 係り先の文節が名詞を含むか
		targetChunk = sentence[dst]
		if targetChunk.existsPart('動詞'):
			print "{0}\t{1}".format(chunk.getText(), targetChunk.getText())
