# -*- coding: utf-8 -*-

import json
import redis

# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ． 

# redisへ接続
conn = redis.StrictRedis(host='localhost', port=6379)

# json読み込み
for line in open("artist.json"):
	obj = json.loads(line)
	
	key = obj['name'] if obj.has_key('name') else ""
	value = obj['area'] if obj.has_key('area') else ""

	# redisにname, areaを保存
	conn.set(key, value)