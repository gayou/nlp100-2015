# -*- coding: utf-8 -*-

from cabocha_parser import CabochaParser


# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

# 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）


filename = "neko.txt.cabocha"

parser = CabochaParser()
parser.parse(filename)

cnt = 0
book = parser.getBook()
for sentence in book:
	dic = {}

	for chunk in sentence:
		# 係り先文節のインデックス
		dst = int(chunk.dst)
		if dst != -1:
			# 係り元文節の形態素リスト
			morphs = chunk.morphs
			for i, morph in enumerate(morphs):
				# 係り元形態素リストのうち、最後から2番目までをチェック
				# 「サ変接続名詞+を（助詞）」で構成される文節かどうかを判定
				if i < len(morphs) - 1 and morph.pos1 == "サ変接続" and morphs[i+1].surface == "を":
					# print "[サ変接続あり]"
					# print chunk.getText()
					# print "  " + sentence[dst].getText()
					pass

				else:
					# サ変接続名詞＋を でない場合は何もしない
					continue

				# 述語を作る
				# 係り先の文節に動詞があるか
				target_chunk = sentence[dst]
				verb = target_chunk.getPart("動詞")
				if verb != None:
					# print "    " + verb.base
					predicate = morph.surface + morphs[i+1].surface + verb.base
				else:
					continue

				# 述語にかかる助詞、文節を取得

				srcs = set(chunk.srcs) if chunk.srcs != None else set([])
				srcs = srcs.union(target_chunk.srcs)
				if len(srcs) == 0:
					continue

				for src in srcs:
					#述語を構成する文節番号は無視する
					if src == chunk.chunk_id:
						continue

					# 文節
					srcChunk = sentence[int(src)]
					postposition = srcChunk.getPart("助詞")
					text = srcChunk.getText()

					if postposition != None:
						if dic.has_key(predicate):
							dic[predicate].append({'postposition':postposition.base, 'text':text})
						else:
							dic[predicate] = [{'postposition':postposition.base, 'text':text}]


	for key, value in dic.iteritems():
		postposition = []
		text = []
		for i in sorted(value):
			postposition.append(i['postposition'])
			text.append(i['text'])

		print "{0}\t{1}\t{2}".format(key, " ".join(postposition), " ".join(text))
