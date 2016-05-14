# -*- coding: utf-8 -*-

import nltk

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 前処理
# sentence = sentence.replace(".", "")

# 単語に分割
# word_list = sentence.split()              # 一番愚直なやり方
# word_list = nltk.word_tokenize(sentence)  # かっこつけてnltk使ったけど、カンマとピリオドがトークンに含まれた
word_list = nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(sentence) # nltkの正規表現使ってトークンに分ける

# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字、それ以外は2文字目を取得
result_list = {}
for i, string in enumerate(word_list):
	add_str = ""
	if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
		add_str = string[0]
	else:
		add_str = string[:2]  # memo: string[0:2]を省略した書き方

	result_list[add_str] = i

print result_list