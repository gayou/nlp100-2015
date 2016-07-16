# -*- coding: utf-8 -*-

from cabocha_parser import CabochaParser


# 文節を表すクラスChunkを実装
# このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つ
# 入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示

filename = "neko.txt.cabocha"

parser = CabochaParser()
parser.parse(filename)

print parser.getSentence(7)