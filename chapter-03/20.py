# -*- coding: utf-8 -*-

import json

# json読み込み
for line in open("jawiki-country.json"):
	obj = json.loads(line)
	
	# title
	title = obj['title']
	# print title
	# print obj['text']

	if title == u"イギリス":
		print obj['text']

