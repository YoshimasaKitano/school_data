## 文字列に関する問題（10問）
# 表示する際は実行結果例を参考に表示してください。

# Q1
# 変数nameに自分の名前を代入
# 変数schoolに文字列"OCA"を代入
# 変数langに文字列"python"を代入する。
""" 実行結果表示例
名前:大阪太郎
学校:OCA
プログラミング言語:python
"""
name = "北野善聖"
school = "OCA"
lang = "python"
print(f"名前:{name}")
print(f"学校:{school}")
print(f"プログラミング言語:{lang}")
print()


# Q2：変数name、変数school、変数langを使って実行結果例のような文章を作成して変数textに代入して表示する
""" 実行結果表示例
私の名前は大阪太郎です。OCAでpythonの学んでいます。
"""
text = "私の名前は" + name + "です。" + school + "で" + lang + "の学んでいます。"
print(text)
print()
# Q3：Q2で作成した変数textの値の文字数を表示
""" 実行結果表示例
変数textの値の文字数:30文字
"""
print(len(text))
print()


# Q4：変数langの値を大文字に変換して表示
""" 実行結果表示例
大文字:PYTHON
"""
print(lang.upper())
print()


# Q5：変数schoolの値を小文字に変換して表示
""" 実行結果表示例
小文字:oca
"""
print(school.lower())
print()


# Q6：Q2で作成した変数textの先頭5文字を表示
""" 実行結果表示例
変数textの先頭5文字:私の名前は
"""
print(text[0:5])
print()

# Q7：Q2で作成した変数textの末尾7文字を表示
""" 実行結果表示例
変数textの末尾5文字:学んでいます。
"""
print(text[-7:])
print()


# Q8：Q2で作成した変数textの値を逆順に表示
""" 実行結果表示例
変数textの値を逆順:。すまいでん学のnohtypでACO。すで郎太阪大は前名の私
"""
print(text[::-1])
print()

# Q9：変数schoolを3回繰り返して表示
""" 実行結果表示例
変数schoolを3回繰り返し:OCAOCAOCA
"""
print(school * 3)
print()

# Q10：任意の文字列を入力、先頭の1文字目と末尾の文字が、一致する場合はTrue、一致しない場合はFalseと表示
""" 実行結果表示例
文字列を入力→php
結果:True
"""
text = input("文字列を入力→")
text[0] ; text[-1]
print(text[0] == text[-1])



