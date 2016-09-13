#!/bin/sh

echo "正例の件数確認"
less rt-polaritydata/rt-polarity.pos | wc -l
less sentiment.txt | grep "^\+1" | wc -l

echo "負例の件数確認"
less rt-polaritydata/rt-polarity.neg | wc -l
less sentiment.txt | grep "^\-1" | wc -l