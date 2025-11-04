#!/bin/bash

#filename:pinging.sh
# ユーザーインターフェース付きのping

echo "PINGを送りたいホスト名またはIPアドレスを入力してください:"
read target

if [ -z "$target" ]: then
	echo "!!! ホスト名が空です。終了します。"
	exit 1
fi

echo "$target に ping を送信中(4回)..."
ping -c 4 "$target"

