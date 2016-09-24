# -*- coding: utf-8 -*-

import codecs
import collections
import math

# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

feature = codecs.open('feature.txt', 'r', 'utf-8', 'ignore')
model   = codecs.open('logistic-model.txt', 'w', 'utf-8')

eta0 = 0.2 #学習率
etan = 0.9999 #学習率減少率
guard = 0.0002 #桁溢れ防止

def sigmoid(x):
	return 1.0 / (1.0 + math.exp(-x))

def update(W, features, label, eta):
	print features
	print "eta=" + str(eta),
	#内積の計算
	a = sum([W[x] for x in features])
	print "a=" + str(a),
	init_feature = 1  
	predict = sigmoid(a)
	print "predict=" + str(predict),
	#ラベルの正規化
	label = (label + 1) / 2
	print "label=" + str(label)

	#重みベクトルの計算
	for x in features:
		dif = eta * ( predict -label ) * init_feature
		print x, dif

		#差が0に近づきすぎると無視
		if (W[x] - dif) > guard or ( W[x] - dif) < (guard * -1):
			W[x] = W[x] - dif


if __name__ == "__main__":
	t = 0
	W = collections.defaultdict(float)

	#重みベクトル計算
	for line in feature:
		features = line[:-1].split(" ")
		update(W, features[1:], float(features[0]), eta0 * ( etan ** t))
		t += 1
		# if t > 10:
		# 	break
		print ""

	#ファイルへ書き出し
	for x in W.items():
		line = "\t".join( map( str,list(x) ) )
		model.writelines(line+"\n")

	# print W