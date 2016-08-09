# -*- coding: utf-8 

# import xml.etree.ElementTree as ET
from lxml import etree

# 入力文中の人名をすべて抜き出せ．

# XMLファイル読み込み
root = etree.parse('nlp.txt.xml', parser=etree.XMLParser())

# NERタグの値がPERSONであるtokenタグを取得
tokens= root.findall("//token[NER='PERSON']")
for token in tokens:
	word  = token.find("word").text
	print word
