# -*- coding: utf-8 -*-

from cabocha_parser import CabochaParser


# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

# 動詞を含む文節において，最左の動詞の基本形を述語とする
# 述語に係る助詞を格とする
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

filename = "neko.txt.cabocha"

parser = CabochaParser()
parser.parse(filename)

book = parser.getBook()
for sentence in book:
	dic = {}
	for chunk in sentence:
		# 係り先文節のインデックス
		dst = int(chunk.dst)
		if dst != -1:
			# 係り元の助詞,係り先の動詞 を表示
			postposition = chunk.getPart("助詞")
			verb = sentence[dst].getPart("動詞")
			if verb != None and postposition != None:
				if dic.has_key(verb.base):
					dic[verb.base].append(postposition.base)
				else:
					dic[verb.base] = [postposition.base]

	for key, value in dic.iteritems():
		value.sort()
		print "{0}\t{1}".format(key, " ".join(value))
				# print "{0}\t{1}".format(verb.base, postposition.base)
			
	# break