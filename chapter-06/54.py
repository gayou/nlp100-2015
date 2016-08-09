# -*- coding: utf-8 

import xml.etree.ElementTree as ET

# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

# XMLファイル読み込み
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

# tokenタグ取得
tokens= root.findall(".//token")
for token in tokens:
	word  = token.find("word").text
	lemma = token.find("lemma").text
	pos   = token.find("POS").text
	print "{0}\t{1}\t{2}".format(word, lemma, pos)
