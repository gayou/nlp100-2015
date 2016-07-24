# -*- coding: utf-8 -*-

from cabocha_parser import CabochaParser


# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．

# 45の仕様に加えて，以下の仕様を満たすようにせよ．
# 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

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
			# 係り元の助詞&テキスト,係り先の動詞 を表示
			postposition = chunk.getPart("助詞")
			text = chunk.getText()
			verb = sentence[dst].getPart("動詞")
			if verb != None and postposition != None:
				if dic.has_key(verb.base):
					dic[verb.base].append({'postposition':postposition.base, 'text':text})
				else:
					dic[verb.base] = [{'postposition':postposition.base, 'text':text}]


	for key, value in dic.iteritems():
		postposition = []
		text = []
		for i in sorted(value):
			postposition.append(i['postposition'])
			text.append(i['text'])


		print "{0}\t{1}\t{2}".format(key, " ".join(postposition), " ".join(text))

