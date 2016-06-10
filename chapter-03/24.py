# -*- coding: utf-8 -*-

import json
import re

# jsonからイギリスに関する記事を取得
text = ""
for line in open("jawiki-country.json"):
	obj = json.loads(line)
	
	# title
	title = obj['title']
	# print title
	# print obj['text']

	if title == u"イギリス":
		text = obj['text']
		# print obj['text']


# 記事から参照されているメディアファイルをすべて抜き出す
match_list = re.findall(u"ファイル:(.+?)\|", text)
for match in match_list:
	# print " "
	print match

match_list = re.findall(u"\[\[ファイル:(.+?)\|", text)
for match in match_list:
	# print " "
	print match