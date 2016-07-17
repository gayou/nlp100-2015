# -*- coding: utf-8 -*-

class Chunk:
	# 形態素リスト
	morphs = []
	# 係り先文節インデックス番号
	dst = ""
	# 係り元文節インデックス番号のリスト
	srcs = []

	# コンストラクタ
	def __init__(self, dst=None):
		self.dst = dst
		self.morphs = []
		self.srcs = []

	# 文節に形態素を追加
	def addMorph(self, morph):
		self.morphs.append(morph)


	def addSrcs(self, src):
		self.srcs.append(src)

	#️ 文節のテキストを返却（記号を除く）
	def getText(self):
		text = ""
		for morph in self.morphs:
			if morph.pos != '記号':
				text += morph.surface
				
		return text

	# 特定の品詞を含むか判定
	def existsPart(self, part):
		exist = False
		for morph in self.morphs:
			if morph.pos == part:
				exist = True
				break

		return exist


	def __str__(self):
		# return "<morph surface='{0.surface}' base='{0.base}' pos='{0.pos}' pos1='{0.pos1}' />".format(self)
		return "<chunk dst='{0}'>\n\t<morphs>{1}</morphs>\n\t<srcs>'{2}'</srcs>\n</chunk>\n".format(self.dst, self.morphs, self.srcs)

	def __repr__(self):
		return self.__str__()
