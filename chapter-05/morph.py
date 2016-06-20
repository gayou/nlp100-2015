# -*- coding: utf-8 -*-

class Morph:
	# 表層形
	surface = ""
	# 基本形
	base = ""
	# 品詞
	pos = ""
	# 品詞細分類1
	pos1 = ""

	def __init__(self, surface=None, base=None, pos=None, pos1=None):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

	def __str__(self):
		# return "<morph surface='{0.surface}' base='{0.base}' pos='{0.pos}' pos1='{0.pos1}' />".format(self)
		return "<morph surface='{0}' base='{1}' pos='{2}' pos1='{3}' />".format(self.surface, self.base, self.pos, self.pos1)

	def __repr__(self):
		return self.__str__()
