# type.py
"""
データ型を調べる
type()

"""
print(type(10)) ### <class 'int'> int型は整数値を表すデータ型
print(type(3.14)) ### <class 'float'> float型は浮動小数点型
print(type("Python")) ### <class 'str'> str型は文字列型

name = "竹國聡子"
print(type(name)) ### <class 'str'>

name = 300
print(type(name)) ### <class 'int'>

name = name / 5
print(type(name)) ### <class 'float'>

print(str(name) + "先生") ### 60.0先生

## データ型を変換する
# 文字列型に変換する str()
num = 10
print(type(num)) ### <class 'int'>

str_num = str(num)
print(str_num) ### 10
print(type(str_num)) ### <class 'str'>

fnum = 3.14
str_fnum = str(fnum)
print(fnum) ### 3.14
print(type(str_fnum)) ### <class 'str'>

# 整数値型に変換する int()
int_num = int(str_num)
print(int_num) ### 10
print(type(int_num)) ### <class 'int'>

"""
name = "竹國先生"
int_name = int(name) ### ValueError
print(int_name)
print(type(int_name))
"""

"""
int_fnum = int(str_fnum) ### ValueError
print(int_fnum)
"""

# 浮動小数点型に変換 float()
f_fnum = float(str_fnum)
print(f_fnum) ### 3.14
print(type(f_fnum)) ### <class 'float'>

int_fnum = int(f_fnum)
print(type(int_fnum)) ### <class 'int'>
print(int_fnum) ### 3 小数点以下が切り捨てられる

f_fnum = float(int_fnum)
print(type(f_fnum)) ### <class 'float'>
print(f_fnum) ### 3.0

## その他の変換
# 2進数に変換
print(bin(10)) ### 0b1010
print(0b1010) ### 10

#8進数に変換
print(oct(10)) ### 0o12
print(0o12) ### 10

# 16進数に変換
print(hex(10)) ### 0xa
print(0xa) ### 10

