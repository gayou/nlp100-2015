# -*- coding: utf-8 -*-

import codecs
import math
import re
import sys
from nltk import stem
from stop_word import StopWord


# 学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．

# シグモイド関数
def sigmoid(x):
	return 1.0 / (1.0 + math.exp(-x))

# ロジスティック回帰モデルを取得
def getLogisticRegressionModel():
	model = {}
	for line in codecs.open('logistic-model.txt', 'r', 'utf-8'):
		line = line.strip().split("\t")
		model[line[0]] = float(line[1])

	return model



# 素性抽出済みのデータを読み込んで予測を行う
model = getLogisticRegressionModel()
review_list = codecs.open('feature.txt', 'r', 'utf-8', 'ignore')
predict = open('predict.txt', 'w')

for review in review_list:
	score = 0
	features = review[:-1].split(" ")
	for feature in features[1:]:
		if feature in model:
			score += model[feature]

	score = sigmoid(score)
	if score >= 0.5:
		result = "+1"
	else:
		result = "-1"

	# 正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力
	print features[0], result, score
	predict.write(features[0] + "\t" + result + "\t" + str(score) + "\n")


predict.close()
