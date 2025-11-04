# comparison.py
"""
論理値(ブール値:bool)と比較演算子
比較演算子を使って比較した結果は論理値(True/False)で返される
"""

a = 3; b = 3; c = 5

# 左右の値が等しい ==
print(a == b) ### True :正しい場合(真)
print(a == c) ### False :間違っている場合(偽)

print(10 == 10) ### True
print(10 == 20) ### False

print("A" == "A") ### True
print("A" == "a") ### False

# 左右の値が等しくない !=
print(a != b) ### False
print(a != c) ### True

# 左が右より大きい >
print(a > b) ### False
print(c > a) ### True

#左が右以上 >=
print(a >= b) ### True

# 左が右より小さい <
print(a < b) ### False
print(a < c) ### True

# 左が右以下 <=
print(a <= b) ### True

t = True
f = False
print(t == f) ### False

