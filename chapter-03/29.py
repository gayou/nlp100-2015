# -*- coding: utf-8 -*-

import codecs
import json
import re
import urllib
import urllib2

# テキストファイル読み込み
text = codecs.open("england.txt", "r").read()

# 国旗画像のURLを取得する
# |国旗画像 = Flag of the United Kingdom.svg
flag = re.findall(r"\|国旗画像 = (.+?)\n", text, re.DOTALL)
title = urllib.quote(flag[0])

# MediaWiki API
url = "https://ja.wikipedia.org/w/api.php?action=query&titles=File:%s&prop=imageinfo&format=json&iiprop=url" % title
response = urllib2.urlopen(url)
jsonstr = response.read()

obj = json.loads(jsonstr)
	
print obj['query']['pages']['-1']['imageinfo'][0]['url']
