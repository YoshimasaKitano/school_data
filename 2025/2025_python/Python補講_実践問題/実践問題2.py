""" 実践問題2
文字列暗号 ― パスワードを変換せよ

[目的]
既知のパスワード文字列 "Zebra123!" に対し、定義されたルールで文字を変換し、暗号化された文字列を生成する。

[入力仕様]
パスワード文字列（固定） "Zebra123!"

[変換ルール]
大文字：1つ後ろのアルファベット（Z → A, A → B）
小文字：2つ前のアルファベット（e → c, b → z）
数字：各桁を2倍し、結果が10以上なら1の位のみ採用（7 → 14 → 4）
記号：そのまま保持

[出力仕様]
変換後の文字列（文字順は保持）
Aczpy246!

[制約]
list構造、関数定義の使用なし
ord() と chr() を用いて文字変換を実装
"""
Pass = "Zebra123!"
for j in Pass:
    j = ord(j)
    if 48 <= j <= 57: # 0～9のUnicode
        j = chr(j)
        j = int(j)
        j *= 2
        if j >= 10:
            j = str(j)
            j = j[-1]
    elif 65 <= j <= 90: # A～ZのUnicode
        if j == 90:
            j = 65
            j = chr(j)
        else:
            j += 1
            j = chr(j)
    elif 97 <= j <= 122: # a～zのUnicode
        if j == 97:
            j = 121
            j = chr(j)
        elif j == 98:
            j = 122
            j = chr(j)
        else:
            j -= 2
            j = chr(j)
    else:               # それ以外(記号など) 
        j = chr(j)
    print(j, end="")


