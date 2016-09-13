# -*- coding: utf-8 -*-

from random import Random

# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

# rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

sentiments = []

# rt-polarity.posの各行の先頭に"+1 "という文字列を追加する
for line in open("rt-polaritydata/rt-polarity.pos"):
	sentiments.append("+1 " + line)

# rt-polarity.negの各行の先頭に"-1 "という文字列を追加する
for line in open("rt-polaritydata/rt-polarity.neg"):
	sentiments.append("-1 " + line)


# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
r = Random()
r.shuffle(sentiments)


# sentiment.txtを作成したら
f = open("sentiment.txt", "w")
for line in sentiments:
	f.write(line)

f.close()