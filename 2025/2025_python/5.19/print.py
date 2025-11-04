# print.py
"""
print()について
"""
print(100) ### 100

a = 200
print(a) ### 200

print(1 + 2) ### 3

a = 100
b = 200
c = 300
print(a + b + c) ### 600

# print()の引数をカンマ「,」で区切る
print(a, b, c) ### 100 200 300

# sep
print(a,b,c,sep=" ") ### 100 200 300
print(a,b,c,sep="/") ### 100/200/300

# end
print(a,b,end="") ### 100 200
print() # 改行
print(c) ### 300
print(400) ### 400

print(a,b,c,sep="/",end="/") ### 100/200/300/以上
print("以上")