# -*- coding: utf-8 -*-

import json
import redis
import sys

# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．

# 引数確認
if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
	print "ERR:コマンドの第1引数に名前を入力してください"
	exit()

# 引数取得
name = sys.argv[1]

# redisへ接続
conn = redis.StrictRedis(host='localhost', port=6379)

# 指定した名前をキーに、活動場所を検索
area = conn.get(name)
print area
# print name, area