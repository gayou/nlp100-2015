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
# 処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）,内部リンクマークアップを除去してテキストに変換
basic_info_str = re.findall(r"{{基礎情報 国(\n|.+?\n)}}\n", text, re.MULTILINE|re.DOTALL)
# print match_list[0]

basic_info_list = basic_info_str[0].split("\n|")
# print basic_info_list

dict = {}
for section in basic_info_list:
	section = section.split(" = ")
	if len(section) == 2:
		key = section[0]
		value = section[1]

		# 強調マークアップを除去する
		value = re.sub(r"\'\'\'\'(.+?)\'\'\'\'", r"\1", value)
		value = re.sub(r"\'\'\'(.+?)\'\'\'", r"\1", value)
		value = re.sub(r"\'\'(.+?)\'\'", r"\1", value)

		# 内部リンクマークアップを除去する
		# [[記事名]]
		# [[記事名|表示文字]]
		# [[記事名#節名|表示文字]]
		value = re.sub(r"\[\[.+?\|.+?\|(.+?)\]\]", r"\1", value)
		value = re.sub(r"\[\[.+?\|(.+?)\]\]", r"\1", value)
		value = re.sub(r"\[\[(.+?)\]\]", r"\1", value)

		# MediaWikiマークアップの除去
		value = re.sub(r"\{\{.+?\|.+?\|(.+?)\}\}", r"\1", value)
		value = re.sub(r"\{\{.+?\|(.+?)\}\}", r"\1", value)

		value = re.sub(r"<ref.+?>.+?</ref>", "", value)
		value = re.sub(r"<ref>.+?</ref>", "", value)
		value = re.sub(r"<ref.+?/>", "", value)
		value = re.sub(r"<br/>", "", value)

		dict[key] = value


# 辞書を表示
for key, value in dict.items():
	print key, value


