# -*- coding: utf-8 -*-

import re

def cipher(string):
	cipher_string = ""
	for char in string:
		if re.match("[a-z]", char):
			cipher_string += unichr(219 - ord(char))
		else:
			cipher_string += char

	return cipher_string


sentence ="Ortiz also delivered a walk-off double in the 11th to become the third player in MLB history to have 500 homers and 600 doubles in his career. The other two are Barry Bonds and Hank Aaron."

print "元のテキスト:"
print sentence
print ""

# 暗号化
sentence_encrypted = cipher(sentence)
print "実行後:"
print sentence_encrypted
print ""
