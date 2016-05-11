# -*- coding: utf-8 -*-

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 前処理
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")

# 単語ごとに配列に分割
sentence_list = sentence.split()
word_count_list = []

for word in sentence_list:
	word_count_list.append(len(word))

print word_count_list

# print sentence_list