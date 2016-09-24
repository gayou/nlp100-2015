# -*- coding: utf-8 -*-

import codecs
import re
import sys
import unicodedata
from nltk import stem
from stop_word import StopWord

reload(sys)
sys.setdefaultencoding('utf-8')

# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
# 素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．

# 学習データ読み込み
sentence = []
for line in codecs.open("sentiment.txt", "r", "utf-8", "ignore"):
	sentence.append(line)


# 素性抽出
sw = StopWord()
stemmer = stem.PorterStemmer()
feature_list = []
for line in sentence:
	line = line.strip()

	# 単語に分割
	feature = []
	word_list = re.compile(r'[,.\s]').split(line)
	for word in word_list:
		if word == '':
			continue

		# ステミング
		word = stemmer.stem(word)
		if sw.isStopWord(word) == False:
			feature.append(word)

	feature_list.append(feature)

# print feature_list


# 素性をファイルに保存
fp = codecs.open("feature.txt", "w", "utf-8")
for feature in feature_list:
	fp.writelines(" ".join(feature))
	fp.write("\n")


