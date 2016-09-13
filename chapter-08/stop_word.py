# -*- coding: utf-8 -*-

class StopWord:
	# ストップワード
	# https://docs.oracle.com/cd/E16338_01/text.112/b61357/astopsup.htm
	stop_word = ["a","all","almost","also","although","an","and","any","are","as","at","be","because","been","both","but","by","can","could","d","did","do","does","either","for","from","had","has","have","having","he","her","here","hers","him","his","how","however","i","if","in","into","is","it","its","just","ll","me","might","Mr","Mrs","Ms","my","no","non","nor","not","of","on","one","only","onto","or","our","ours","s","shall","she","should","since","so","some","still","such","t","than","that","the","their","them","then","there","therefore","these","they","this","those","though","through","thus","to","too","until","ve","very","was","we","were","what","when","where","whether","which","while","who","whose","why","will","with","would","yet","you","your","yours"]

	# コンストラクタ
	def __init__(self):
		pass

	# ストップワードかどうか判定
	def isStopWord(self, str):
		return str in self.stop_word
