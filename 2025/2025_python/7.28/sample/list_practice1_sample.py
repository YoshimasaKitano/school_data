# リストの練習問題
### 問題1：0から20までの乱数を10個要素に持つリストを繰返し構文を使って作成する
from random import randint

list_data = []
for i in range(10):
    list_data.append(randint(0,20))

print(list_data)

# リスト内包表記
list_data = [randint(0,20) for i in range(10)]
print(list_data)


### 問題2：問題1のリストから偶数だけのリストを作る
odd_list = []
for i in list_data: # リストから順に要素を取り出す
    if i%2==0: # 要素が偶数の場合
        odd_list.append(i) # リストに追加する

print(odd_list)


### 問題3：問題1のリストの要素の合計値、最大値、最小値、平均値の計算
print(f"合計値:{sum(list_data)}")
print(f"最大値:{max(list_data)}")
print(f"最小値:{min(list_data)}")
print(f"平均値:{sum(list_data)/len(list_data)}")


### 問題4：問題1のリストの並び替え（昇順）
print(f"昇順:{sorted(list_data)}")


### 問題5：問題1のリストの最初の要素と最後の要素の合計値を表示
print(f"最初の要素:{list_data[0]}")
print(f"最後の要素:{list_data[-1]}")
print(f"合計値:{list_data[0]+list_data[-1]}")


