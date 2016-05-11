# -*- coding: utf-8 -*-

str1 = u"パトカー"
str2 = u"タクシー"

answer = u""
for i, str in enumerate(str1):
	answer += str + str2[i]

print answer
