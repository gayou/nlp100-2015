# -*- coding: utf-8 -*-

import sys
import pydot
from cabocha_parser import CabochaParser

reload(sys)  
sys.setdefaultencoding('utf8')


# 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

# 指定したインデックスの文の係り受け木のグラフを作る
idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# Cabocha解析結果のファイルをパース
filename = "neko.txt.cabocha"

parser = CabochaParser()
parser.parse(filename)

# 対象とする文章
edges = []
sentence = parser.getBook()[idx]
for chunk in sentence:
	dst = int(chunk.dst)
	if dst != -1:
		# 係り元のテキスト,係り先のテキスト を表示
		textFrom = chunk.getText()
		textTo = sentence[dst].getText()
		edges.append((textFrom, textTo))
		print "{0}\t{1}".format(chunk.getText(), sentence[dst].getText())

g = pydot.graph_from_edges(edges)
g.write_jpeg('44.jpg', prog='dot')

