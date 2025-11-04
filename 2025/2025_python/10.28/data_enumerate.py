### data_enumerate.py
"""
テキストファイルからカンマ区切りでデータを読み込んで各行ごとに値の判定を行う
2.0以下は1、それ以上は0
"""

file = "./10.28/numdata.txt"
limit = 2.0

with open(file, "r", encoding = "utf-8") as fileobj:
    for i, line in enumerate(fileobj):

        if line == "\n": # 改行コードで1行の終わり
            continue

        datalist = line.split(",")
        print(datalist)

        resultlist = []
        for num in datalist:
            if float(num) <= limit: # 数字を数値に変換して比較
                resultlist.append(1)
            else:
                resultlist.append(0)
        print(f"{i}:{resultlist}")