# -*- coding: utf-8 -*-

from stop_word import StopWord

# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
# さらに，その関数に対するテストを記述せよ．

# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
# → StopWord.isStopWord を実装


# テスト
sw = StopWord()

print sw.isStopWord("and")
print sw.isStopWord("andrew")