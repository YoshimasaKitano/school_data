# try_sample.py
"""
try文 例外処理
エラーが発生する可能性がある場合の事前処理
"""
from ast import While


a = 10
# a / b # NameError: name 'b' is not defined

b = 0
# a / b # ZeroDivisionError: division by zero

# num = int("100個") # ValueError: invalid literal for int() with base 10: '100個'

## 整数値を入力してください
while True: # 無限ループ

    try:
        # エラーが発生する可能性がある処理
        num = int(input("整数値を入力してください→"))
        break # 正しく入力された場合は繰り返しから抜ける

    except:
        # エラーが発生した場合の処理
        print("正しい数値を入力してください。")

print(num)

## 正の整数値を入力してください。
while True:

    try:
        num = int(input("正の整数値を入力してください→"))
        if num < 0:
            print("0以上の数値を入力してください。")
            continue

        break

    except:
        print("正しい数値を入力してください")

    finally:
        print("例外が発生しても、しなくても実行する")

print(num)


"""練習
数値を5回入力し、合計を表示する
"""
count = 1
result = 0
while count < 5:

    try:
        num = int(input("数値を入力してください"))

    except:
        print("正しい数値を入力してください")
        continue

        
    result = result + num

    count += 1

print(result)

"""
2つの数値を入力し、割った商と余りを表示する
"""

try:
    numA = int(input("1つ目の数値を入力→"))
    numB = int(input("2つ目の数値を入力→"))

    division = numA // numB
    remainder = numA % numB



except ValueError as e1: # 例外に名前を付ける
    print("入力に問題が発生しました。")
    print(e1) # 例外の情報を表示する
     
except ZeroDivisionError as e2:
    print("0で割ることはできません。")
    print(e2)

except:
    print("値を正しく取得できません。")

else: # 例外の発生なく正しく実行された場合に実行される
    print(   print(f"{numA} ÷ {numB}は、{division}と余り{remainder}"))

finally: # 例外があってもなくても実行される
    print("処理を終了します")