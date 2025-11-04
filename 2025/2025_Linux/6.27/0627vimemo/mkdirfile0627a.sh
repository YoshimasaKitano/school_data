#!/bin/bash

#FILENAME:makedirfile0607a.sh

rm -rf ~/0627a

mkdir ~/0627a/project/src/html/html -p
mkdir ~/0627a/project/src/html/media
mkdir ~/0627a/project/src/html/css
mkdir ~/0627a/project/src/python
mkdir ~/0627a/docs

ln -s /var/www/html ~/0627a/webroot

touch ~/0627a/project/src/html/html/index.html
touch ~/0627a/project/src/html/html/forms.html
touch ~/0627a/project/src/html/html/result.html
touch ~/0627a/project/src/html/media/oca.png
touch ~/0627a/project/src/html/media/ktc.png
touch ~/0627a/project/src/html/media/nca.png
touch ~/0627a/project/src/html/css/style.css
touch ~/0627a/project/src/html/css/layout.css
touch ~/0627a/project/src/html/css/main.css
touch ~/0627a/project/src/python/hello.py
touch ~/0627a/docs/readme.txt
touch ~/0627a/docs/project_outline.txt
touch ~/0627a/docs/config.txt

cd ~/0627a
pwd
tree

echo ""
echo "ファイルとフォルダが正常に作成されました。"
echo ""
