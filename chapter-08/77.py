# -*- coding: utf-8 -*-

import codecs
import math
import re
import sys
from nltk import stem
from stop_word import StopWord


# 76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．

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


# 予測結果のファイルを読み込む
predict_list = open('predict.txt', 'r')

# 問題数
count = 0
positive_count = 0
#F-mesure
tp = 0
fp = 0
fn = 0
tn = 0

for predict in predict_list:
	predict = predict[:-1].split("\t")

	# 問題数をカウント
	count += 1
	if predict[0] == "+1":
		positive_count += 1

	# F-mesure値をカウントアップ
	if predict[0] == "+1":
		if predict[1] == "+1":
			tp += 1
		else:
			fn += 1
	else:
		if predict[1] == "+1":
			fp += 1
		else:
			tn += 1


print "問題数:", count
print "正解数:", tp + tn
print "正解率:", float(tp + tn) / float(count)
print "-------"

precision = float(tp) / float(tp + fp)
recall = float(tp) / float(tp + fn)

print "適合率:", precision
print "再現率:", recall
print "F値　 :", (2 * precision * recall) / (precision + recall)
