# -*- coding: utf-8 -*-

from chunk import Chunk
from morph import Morph
import codecs
import re

class CabochaParser:
	# 解析結果
	parsed = []

	def __init__(self):
		pass

	# cabochaの解析ファイルをパース
	def parse(self, filename):
		book = []
		sentence = []
		chunk = Chunk()
		srcs = {}

		cnt_eos = 0
		for line in codecs.open(filename, "r"):
			# 文節の始まり
			if line[0] == '*':
				# print line
				column = line.split(" ")
				chunck_id = str(column[1])

				if chunck_id != '0':
					sentence.append(chunk)

				# 係り先
				dst = column[2].replace("D", "")
				if dst != '-1':
					if srcs.has_key(dst):
						srcs[dst].append(chunck_id)
					else:
						srcs[dst] = [chunck_id]

				# Chunkオブジェクト生成
				chunk = Chunk()
				chunk.dst = dst
				chunk.srcs = srcs.get(chunck_id)

				continue

			# 一文の終わりの場合
			if line.strip() == 'EOS':
				cnt_eos += 1
				if len(sentence) > 0:
					sentence.append(chunk)
					book.append(sentence)
					# print chunk
					sentence = []
					srcs = {}

				continue

			# 文の開始または途中の場合
			column = re.split("[\t|,]", line)
			morpheme = Morph(column[0], column[7], column[1], column[2])
			chunk.addMorph(morpheme)

		self.parsed = book


	def getBook(self):
		return self.parsed

	def getSentence(self, index):
		return self.parsed[index]

