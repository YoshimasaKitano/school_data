# string_slice.py
"""
文字列のスライス
"""
id = "abcdefghi"

print(id[2]) ### c
print(id[5]) ### f

char = id[4]
print(char) ### e

print(id)

"""変更はできない
id[0] = "x"
print(id)
"""

## 範囲を指定してスライスする
s = "The quick brown fox jumps over the lazy dog."

# s[開始位置:終了位置]
print(s[2:6]) ### e qu
print(s[4:9]) ### quick

# 全部
print(s[:]) ### The quick brown fox jumps over the lazy dog.

# 開始位置から後ろ全部
print(s[11:]) ### rown fox jumps over the lazy dog.

# 終了位置から前全部
print(s[:11]) ### The quick b

# 指定場所から指定文字数分
print(s[10:10+5]) ### brown

# 後ろから範囲を指定する
print(s[:-19]) ### The quick brown fox jumps
print(s[-18:-1]) ### over the lazy dog

# 文字数を数える len()
print(len(s)) ### 44

"""# 文字数を超えた位置指定
print(s[50]) ### IndexError
"""

# 文字数を超えた範囲指定
print(s[:50]) ### The quick brown fox jumps over the lazy dog.
num = "0123456789"
## ステップ値
# 文字列[開始位置:終了位置:ステップ値]
print(num[:]) ### 0123456789
print(num[::]) ### 0123456789
print(num[::1]) ### 0123456789
print(num[::2]) ### 02468
print(num[1::2]) ### 13579
print(num[::-1]) ### 9876543210
