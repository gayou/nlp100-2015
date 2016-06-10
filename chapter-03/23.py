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


# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示
match_list = re.findall("(={2,})\s*(.+?)={1,}", text)
# section = match.groups()[0]
for match in match_list:
	print match[1],len(match[0])