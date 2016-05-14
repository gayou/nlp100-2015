# -*- coding: utf-8 -*-

def createSentence(x, y, z):
	# return str(x) + "時の" + str(y) + "は" + str(z)
	return u"{x}時の{y}は{z}".format(x=x, y=y, z=z)


print createSentence(12, u"気温", 22.4)