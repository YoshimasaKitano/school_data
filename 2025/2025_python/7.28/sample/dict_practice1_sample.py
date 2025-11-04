### 問題1：商品管理システム（在庫の表示）

""" 仕様  
以下のような辞書で商品と在庫数を管理している。すべての商品名と在庫数を表示するプログラムを書いてください。  

[python]
inventory = {"apple": 5, "banana": 2, "orange": 8}

[結果例]
appleは、5
bananaは、2
orangeは、8
"""
inventory = {"apple": 5, "banana": 2, "orange": 8}

## sample1
for key in inventory: # 繰り返し辞書からキーを取得
    print(key + "は、" + str(inventory[key])) # キーを指定して値も取得

## sample2
for key in inventory.keys(): # 繰り返し辞書からキーを取得
    print(key + "は、" + str(inventory[key])) # キーを指定して値も取得

## sample3
for key,value in inventory.items(): # items()メソッドでキーと値を取得
    print(f"{key}は、{value}")


### 問題2：お気に入り登録システム

""" 仕様  
ユーザーの「お気に入り」アイテムを辞書で管理している。  
例えば次のような辞書：  

[python]
favorites = {"user1": "ラーメン", "user2": "寿司"}
  
この辞書に "user3": "うどん" を追加し、その内容をすべて表示してください。
"""
favorites = {"user1": "ラーメン", "user2": "寿司"}

favorites["user3"] = "うどん" # キーを設定して値を代入
print(favorites)


### 問題3：簡単なスコア集計

""" 仕様  
以下の辞書には教科ごとの点数が入っています。合計点と平均点を計算して出力してください。  

[python]
scores = {"math": 85, "english": 78, "science": 92}

[結果]
合計:
平均:
"""
scores = {"math": 85, "english": 78, "science": 92}

total = 0
for key in scores.keys(): # 繰り返しキーを取得
    total += scores[key] # キーから値を取得して加算していく

print(f"合計:{total}")
print(f"平均:{total/len(scores)}") # 合計を要素数で割る

### 問題4：ユーザー情報の更新

""" 仕様  
ユーザーの情報を辞書で管理している。次のような辞書：  

[python]
user = {"name": "Taro", "age": 20, "city": "Osaka"}

このユーザーの "age" を 21 に更新し、その辞書全体を出力してください。
"""
user = {"name": "Taro", "age": 20, "city": "Osaka"}
if "age" in user: # user内に"age"があれば
    user["age"] = 21 # キーを指定して値を更新

print(user)


### 問題5：複数ユーザーの名前の一覧を表示

""" 仕様  
複数のユーザー情報が辞書のリストとして格納されている。全ユーザーの名前と年齢を表示してください。  

[python]
users = [
    {"name": "Yuki", "age": 19},
    {"name": "Hana", "age": 18},
    {"name": "Ken", "age": 20}
]

[結果例]
名前:Yuki、年齢:19
名前:Hana、年齢:18
名前:Ken、年齢:20
"""
users = [
    {"name": "Yuki", "age": 19},
    {"name": "Hana", "age": 18},
    {"name": "Ken", "age": 20}
]

for d in users: # usersリストから要素(辞書型)を取り出す
    # 取り出した辞書型からキーを指定して値を取り出す
    print(f"名前:{d['name']}、年齢:{d['age']}")


