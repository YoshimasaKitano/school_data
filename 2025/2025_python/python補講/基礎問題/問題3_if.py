## if文に関する問題（10問）
# 以下の乱数は各問題で使用します。変更しないでください。
from random import randint
numA = randint(-50,50)
numB = randint(-50,50)
numC = randint(1,99)
print("数値A:"+str(numA)+" 数値B:"+str(numB)+" 数値C:"+str(numC))
print()


### 低レベル
# Q1：数値Aと数値Bの差は、正の整数か負の整数か表示
""" 実行結果表示例
数値の差:81で正の整数
"""
ans = numA - numB
if ans > 0:
    print(f"数値の差:{ans}で正の整数")
else:
    print(f"数値の差:{ans}で負の整数")
print()


# Q2：数値Aと数値Bの合計は、奇数か偶数か表示する。ただし、0の場合は"0です"と表示
""" 実行結果表示例
数値の合計:9で奇数
"""
ans = numA + numB
if ans != 0:
    if ans % 2 == 0:
        print(f"数値の合計:{ans}で偶数")
    else:
        print(f"数値の合計:{ans}で奇数")
else:
    print("0です")
print()



# Q3：数値Aと数値Bの2つの値の一致判定
""" 実行結果表示例
2つの数値は、不一致
"""
if numA == numB:
    print("2つの数値は、一致")
else:
    print("2つの数値は、不一致")
print()

# Q4：文字列が空かどうか判定
""" 実行結果表示例
入力→a
何か入力されています

入力→
空文字です
"""
text = input("入力→")
if len(text) == 0:
    print("空文字です")
else:
    print("何か入力されています")
print()



### 中レベル
# Q5：数値Aと数値Bの平均値が正の偶数か正の奇数か負の偶数か負の奇数かどうか判定
""" 実行結果表示例
数値の平均値:4.5 正の奇数
"""
ans = (numA + numB) / 2
if ans > 0:
    if ans % 2 == 0:
        print(f"数値の平均値:{ans} 正の偶数")
    else:
        print(f"数値の平均値:{ans} 正の奇数")
else:
    if ans % 2 == 0:
        print(f"数値の平均値:{ans} 負の偶数")
    else:
        print(f"数値の平均値:{ans} 負の奇数")
print()



# Q6：数値A、数値B、数値Cの中で最大値はどれかを表示
""" 実行結果表示例
最大値は数値A
"""
if numA > numB and numA > numC:
    print("最大値は数値A")
elif numB > numA and numB > numC:
    print("最大値は数値B")
else:
    print("最大値は数値C")

# Q7：変数numCを年齢として区分表示する
# 0～18歳未満:未成年 18～64未満:成人 65～高齢者, 75以上:後期高齢者
""" 実行結果表示例
8歳は未成年です。
"""
if numC < 18:
    print(f"{numC}歳は未成年です")
elif 18 <= numC < 64:
    print(f"{numC}歳は成人です")
elif 65 <= numC < 75:
    print(f"{numC}歳は高齢者です")
else:
    print(f"{numC}歳は後期高齢者です")
print()



    
### 高レベル
# Q8：変数numCの値が3の倍数かつ偶数かどうか判定（条件成立 / 条件不成立）
""" 実行結果表示例
条件不成立
"""
if numC % 3 == 0 and numC % 2 == 0:
    print("条件成立")
else:
    print("条件不成立")


# Q9：IDとパスワード入力、一致判定
setId=1234;setPass="abcd"
""" 実行結果表示例
ID(数値4ケタ)を入力→1234
パスワードを入力→abcd
認証結果:認証成功

ID(数値4ケタ)を入力→4321
パスワードを入力→abcd
認証結果:IDが違います。

ID(数値4ケタ)を入力→1234
パスワードを入力→dcba
認証結果:パスワードが違います

ID(数値4ケタ)を入力→1111
パスワードを入力→aaaa
認証結果:IDとパスワードが違います。
"""
try:
    numId = int(input("ID(数値4ケタ)を入力→"))
    strPass = input("パスワードを入力→")
    if numId == setId and strPass == setPass:
        print("認証結果:認証成功")
    elif numId != setId and strPass == setPass:
        print("認証結果:IDが違います。")
    elif numId == setId and strPass != setPass:
        print("認証結果:パスワードが違います")
    else:
        print("認証結果:IDとパスワードが違います。")
except:
    print("IDは数値で入力してください")



# Q10：小数が整数かどうか判定
""" 実行結果表示例
数値を入力→3
3.0は整数です

数値を入力→3.14
3.14は小数です
"""
num = float(input("数値を入力→"))
ans = num * 10
if ans % 10 == 0:
    print(f"{num}は整数です")
else:
    print(f"{num}は小数です")


