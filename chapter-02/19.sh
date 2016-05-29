#!/bin/sh

cut -f1 hightemp.txt | sort | uniq -c | sort -rnk1