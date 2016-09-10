# -*- coding: utf-8 -*-

import json
import redis
import sys

# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

# 引数確認
if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
	print "ERR:コマンドの第1引数に名前を入力してください"
	exit()

# 引数取得
name = sys.argv[1]

# redisへ接続
conn = redis.StrictRedis(host='localhost', port=6379, db=1)

# 指定した名前をキーに、タグを出力
tags = conn.get(name)
tags = json.loads(tags)
for tag in tags:
	print tag['value'], tag['count']
