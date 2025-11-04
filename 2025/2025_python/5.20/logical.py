# logical.py
"""
論理演算子 「and」「or」「not」
"""
# 左右がTrueの場合True 論理積 ～かつ～
print(True and True) ### True
print(True and False) ### False
print(False and False) ### False

a = 80
print(a > 50 and a < 100) ### True

print(50 < a < 100) ### True

b = 40
print(b > 50 and b < 100) ### False

print(50 < b < 100) ### False

print(1 and 1) ### 1
print(1 and 0) ### 0
print(0 and 0) ### 0

# or 左右のどちらかがTrueの場合True 論理和 ～または～
print(True or True) ### True
print(True or False) ### True
print(False or False) ### False

a = 80
print(a > 50 or a < 100) ### True

b = 40
print(b > 50 or b < 100) ### True

print(1 or 1) ### 1
print(1 or 0) ### 1

# not 否定
print(not True) ### False
print(not False) ### True
