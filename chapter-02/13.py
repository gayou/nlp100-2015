# -*- coding: utf-8 -*-

import codecs

fh2 = codecs.open("col2.txt", "r", "utf-8")
fh1and2 = codecs.open("col1and2.txt", "w", "utf-8")
for line1 in codecs.open("col1.txt", "r", "utf-8"):
	# col1.txtの内容
	line1 = line1[:-1]
	# col2.txtの内容
	line2 = fh2.readline()[:-1]
	
	# col1とcol2をタブ区切りでくっつけてファイル出力
	fh1and2.write(line1 + "\t" + line2 + "\n")

fh2.close()
fh1and2.close()