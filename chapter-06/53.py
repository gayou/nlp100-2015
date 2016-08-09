# -*- coding: utf-8 

import xml.etree.ElementTree as ET

# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
# cd 
# java -Xmx5g -cp stanford-corenlp-3.6.0.jar:stanford-corenlp-models-3.6.0.jar:* edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,mention,coref -file /path/to//nlp.txt -outputFormat xml
# cp -p nlp.txt.xml /path/to/
#
# また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．


# XMLファイル読み込み
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

# wordタグ取得
words= root.findall(".//word")
for word in words:
	print word.text
