# -*- coding: utf-8 -*-

import codecs
import math
import re
import sys
from nltk import stem
from stop_word import StopWord


# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．

# シグモイド関数
def sigmoid(x):
	return 1.0 / (1.0 + math.exp(-x))

# 素性抽出
def getFeature(sentence):
	sw = StopWord()
	stemmer = stem.PorterStemmer()

	feature = []

	# 単語に分割
	sentence = sentence.strip()
	word_list = re.compile(r'[,.\s]').split(sentence)
	for word in word_list:
		if word == '':
			continue

		# ステミング
		word = stemmer.stem(word)
		if sw.isStopWord(word) == False:
			feature.append(word)

	return feature

# ロジスティック回帰モデルを取得
def getLogisticRegressionModel():
	model = {}
	for line in codecs.open('logistic-model.txt', 'r', 'utf-8'):
		line = line.strip().split("\t")
		model[line[0]] = float(line[1])

	return model



# 引数確認
print 'Input sentence review of movie.'
sentence = raw_input('>>>  ')
if len(sentence) == 0:
	print "Input sentence review of movie!!"
	exit()


# 素性抽出
features = getFeature(sentence)

# 予測
score = 0
model = getLogisticRegressionModel()
for feature in features:
	if feature in model:
		score += model[feature]

# 結果出力
score = sigmoid(score)
if score >= 0.5:
	print "+1",
else:
	print "-1",

print ", p=" + str(score)


# sentences = codecs.open('feature.txt', 'r', 'utf-8', 'ignore')
# for line in sentences:
# 	score = 0
# 	features = line[:-1].split(" ")
# 	for feature in features[1:]:
# 		if feature in model:
# 			score += model[feature]

# 	score = sigmoid(score)

# 	print " ".join(features[1:])
# 	print "正解:", features[0],
# 	print "予測:",
# 	if score >= 0.5:
# 		print "+1",
# 	else:
# 		print "-1",
# 	print "　(スコア:", score, ")"
# 	print ""
