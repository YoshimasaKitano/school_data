# numeric.py
"""
数値について
"""
# 整数
a = +10 # 正の整数
b = -20 # 負の整数
c = a + b
print(c) ### -10


#浮動小数点
a = 0.08
b = 98.5
c = -3.5
print(a,b,c) ### 0.08 98.5 -3.5
print(a + b + c) ### 95.08

a = .08
print(a) ### 0.08

print(10.) ### 10.0

# 値の大きな数値
a = 1230000000000
print(a) ### 1230000000000

a = 123e10
print(a) ### 1230000000000.0

a = 123e+10
print(a) ### 1230000000000.0

b = 0.008e+5
print(b) ### 800.0

# 浮動小数点の計算
print(10.3 + 0.5) ### 10.8
print(120 * 0.3) ### 36.0
print(100 / 4) ### 25.0

# まるめ処理 round()
print(round(1.4)) ### 1
print(round(1.5)) ### 2
print(round(2.5)) ### 2
print(round(2.6)) ### 3
print(round(3.5)) ### 4
print(round(4.5)) ### 4
print(round(5.5)) ### 6

