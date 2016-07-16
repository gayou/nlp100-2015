# -*- coding: utf-8 -*-

from cabocha_parser import CabochaParser


# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

filename = "neko.txt.cabocha"

parser = CabochaParser()
parser.parse(filename)

book = parser.getBook()
for sentence in book:
	for chunk in sentence:
		# 係り先文節のインデックス
		dst = int(chunk.dst)
		if dst != -1:
			# 係り元のテキスト,係り先のテキスト を表示
			print "{0}\t{1}".format(chunk.getText(), sentence[dst].getText())

	# break