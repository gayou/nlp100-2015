# -*- coding: utf-8 -*-

def ngram(tokens, n):
	# print token
	ngram_list = []
	for i in range(len(tokens) - 1):
		ngram_list.append((tokens[i], tokens[i+1]))

	return ngram_list


sentence1 = "paraparaparadise"
sentence2 = "paragraph"

x = ngram(sentence1, 2)
y = ngram(sentence2, 2)

print "x = ", x
print ""

print "y = ", y
print ""

# 和
print "x + y = ", list(set(x) | set(y))
print ""

# 差
print "x - y = ", list(set(x) - set(y))
print ""

# 積
print "x * y = ", list(set(x) & set(y))
print ""

# se というbi-gramが存在するか
if ("s", "e") in x:
	print "xに se というbi-gramが存在する"
else:
	print "xに se というbi-gramが存在しない"

if ("s", "e") in y:
	print "yに se というbi-gramが存在する"
else:
	print "yに se というbi-gramが存在しない"