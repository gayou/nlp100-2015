#!/bin/bash

# 73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．

# 重みの高い素性トップ10
echo "重みの高い素性トップ10"
less logistic-model.txt | sort -k2 -nr | head -n 10
# paste <(cut -f2 logistic-model.txt) <(cut -f1 logistic-model.txt) | sort -nr | head -n 10

echo ""

echo "重みの低いトップ10"
less logistic-model.txt | sort -k2 -n | head -n 10
# paste <(cut -f2 logistic-model.txt) <(cut -f1 logistic-model.txt) | sort -n | head -n 10