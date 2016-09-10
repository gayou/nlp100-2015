# -*- coding: utf-8 -*-

import json
import redis

# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

# redisへ接続
conn = redis.StrictRedis(host='localhost', port=6379, db=1)

# json読み込み
for line in open("artist.json"):
	obj = json.loads(line)
	
	key = obj['name'] if obj.has_key('name') else ""
	value = obj['tags'] if obj.has_key('tags') else []

	# redisにname, areaを保存
	conn.set(key, json.dumps(value))
