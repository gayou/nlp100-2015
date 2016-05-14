# -*- coding: utf-8 -*-

import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# nltkの正規表現使ってトークンに分ける
# word_list = nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(sentence)

word_list = sentence.split()

new_word_list = []
for word in word_list:
	# 長さが４以上の単語は、先頭と最後の文字以外をランダムに並び替える
	if len(word) > 4:
		char_list = list(word[1:-1])
		# 先頭と最後の文字以外をランダムに並び替え
		random.shuffle(char_list)
		word = word[0] + "".join(char_list) + word[-1]

	new_word_list.append(word)


print " ".join(new_word_list)