# -*- coding: utf-8 -*-

import nltk

def ngram(tokens, n):
	# print token
	ngram_list = []
	for i in range(len(tokens) - 1):
		ngram_list.append([tokens[i], tokens[i+1]])

	return ngram_list


sentence = "I am an NLPer"

# word bi-gram
# word_token = nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(sentence)
word_token = sentence.split()
print ngram(word_token, 2)

print ""

# char bi-gram
print ngram(sentence, 2)