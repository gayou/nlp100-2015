#!/bin/sh


echo "コーパス中で頻出する述語と格パターンの組み合わせ"
less neko.txt.cabocha.45.txt | sort | uniq -c | sort -r -t\t -k1 | head -n 30
echo ""

echo "「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べる）"
# less neko.txt.cabocha.45.txt | grep -E "^(する|見る|与える)\t" | sort | uniq -c | sort -r -t\t -k1 | head -n 10


echo "する"
less neko.txt.cabocha.45.txt | grep -E "^する\t" | sort | uniq -c | sort -r -t\t -k1 | head -n 10
echo ""

echo "見る"
less neko.txt.cabocha.45.txt | grep -E "^見る\t" | sort | uniq -c | sort -r -t\t -k1 | head -n 10
echo ""

echo "与える"
less neko.txt.cabocha.45.txt | grep -E "^与える\t" | sort | uniq -c | sort -r -t\t -k1 | head -n 10
