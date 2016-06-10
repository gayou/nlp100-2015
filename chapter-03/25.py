# -*- coding: utf-8 -*-

import codecs
import json
import re

# jsonからイギリスに関する記事を取得
# text = ""
# fh_england = codecs.open("england.txt", "w", "utf-8")
# for line in open("jawiki-country.json"):
# 	obj = json.loads(line)
	
# 	# title
# 	title = obj['title']
# 	# print title
# 	# print obj['text']

# 	if title == u"イギリス":
# 		text = obj['text']
# 		# print text
# 		fh_england.write(text)

# fh_england.close()

# テキストファイル読み込み
text = codecs.open("england.txt", "r").read()

# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納
basic_info_str = re.findall(r"{{基礎情報 国(\n|.+?\n)}}\n", text, re.MULTILINE|re.DOTALL)
# print match_list[0]

basic_info_list = basic_info_str[0].split("\n|")
print basic_info_list

for section in basic_info_list:
	# print section.replace("\n", "")
	print section
	print "==================="
