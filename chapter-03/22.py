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


# カテゴリ名を抽出
text_lines = text.split("\n")
# print text_lines
for line in text_lines:
	# print line
	match = re.match("\[\[Category:(.*)\]\]", line)
	if match != None:
		# print match
		category = match.groups()[0]
		print category.split("|")[0]