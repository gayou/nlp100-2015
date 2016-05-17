# -*- coding: utf-8 -*-

import codecs

fh1 = codecs.open("col1.txt", "w", "utf-8")
fh2 = codecs.open("col2.txt", "w", "utf-8")
for line in codecs.open("hightemp.txt", "r", "utf-8"):
	line = line[:-1].split()
	print line

	fh1.write(line[0] + "\n")
	fh2.write(line[1] + "\n")


fh1.close()
fh2.close()