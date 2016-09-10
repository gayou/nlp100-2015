# -*- coding: utf-8 -*-

import json
import redis

# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．

area = "Japan"

# redisへ接続
conn = redis.StrictRedis(host='localhost', port=6379)

# area=Japanのものを検索
count = 0
keys = conn.scan_iter()
for key in keys:
	# area=Japanか？
	if conn.get(key) == "Japan":
		# print key
		count += 1

print "-------------"
print "アーティスト数: " + str(count)