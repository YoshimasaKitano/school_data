#!/bin/bash

# filename:calc.sh
# 簡単な足し算電卓

echo "数値Aを入力:"
read a
echo "数値Bを入力:"
read b
sum=$((a+b))

echo "合計は $sum です。"

