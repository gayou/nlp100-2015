# -*- coding: utf-8 

# import xml.etree.ElementTree as ET
from lxml import etree

# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
# ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

# XMLファイル読み込み
root = etree.parse('nlp.txt.xml', parser=etree.XMLParser())

# sentenceタグ単位で処理
sentence_list = root.xpath("//sentences/sentence")
for sentence in sentence_list:
	sentence_id = int(sentence.get("id"))
	# print str(sentence_id) + ":",

	# 文中の参照表現（mention）に代表参照表現（representative mention）があるか
	# coreference/coreferenceから探す
	target_mentions = []
	coreference = root.xpath("//coreference/coreference[mention[not(@representative)][sentence[text()='" + str(sentence_id) + "']]]")
	if len(coreference) > 0:
		target_mentions = coreference[0].xpath("mention[not(@representative)][sentence[text()='" + str(sentence_id) + "']]")
		representative  = coreference[0].xpath("mention[@representative]/text")[0].text

	# tokenタグ単位
	tokens = sentence.xpath("tokens/token")
	for token in tokens:
		token_id = int(token.get("id"))

		# 参照表現かどうか
		is_mention = False
		if len(target_mentions) > 0:
			for mention in target_mentions:
				start = int(mention.find("start").text)
				end   = int(mention.find("head").text)
				# 参照表現の場合はテキストをすぐに出力しない
				if token_id >= start and token_id < end:
					is_mention = True
					pass

				# 参照表現の最後でテキストを出力
				elif token_id == end:
					# 代表参照表現（参照表現）の形式で出力
					is_mention = True
					print representative + "(" + mention.find("text").text + ")",


		# 参照表現のテキストでないものはそのまま出力
		if is_mention == False:
			print token.find("word").text,

	print ""
	print ""
