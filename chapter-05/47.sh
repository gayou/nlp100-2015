#!/bin/sh

# 47.pyを実行
python 47.py > neko.txt.cabocha.47.txt

echo "コーパス中で頻出する述語"
less neko.txt.cabocha.47.txt | cut -f1 | sort | uniq -c | sort -r | head -n 30
echo ""

echo "コーパス中で頻出する述語と助詞パターン"
less neko.txt.cabocha.47.txt | cut -f1,2 | sort | uniq -c | sort -r | head -n 30
