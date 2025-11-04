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
for key, value in inventory.items():
    print(f"{key}は、{value}")

"""模範解答
"""
# inventory = {"apple": 5, "banana": 2, "orange": 8}

# for key in inventory

### 問題2：お気に入り登録システム

""" 仕様  
ユーザーの「お気に入り」アイテムを辞書で管理している。  
例えば次のような辞書：  

[python]
favorites = {"user1": "ラーメン", "user2": "寿司"}
  
この辞書に "user3": "うどん" を追加し、その内容をすべて表示してください。
"""
favorites = {"user1": "ラーメン", "user2": "寿司"}
favorites["user3"] = "うどん"
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
total_value = 0
for key, value in scores.items():
    total_value += value
avarage_value = total_value / len(scores)
print(f"合計：{total_value}")
print(f"平均：{avarage_value}")

### 問題4：ユーザー情報の更新

""" 仕様  
ユーザーの情報を辞書で管理している。次のような辞書：  

[python]
user = {"name": "Taro", "age": 20, "city": "Osaka"}

このユーザーの "age" を 21 に更新し、その辞書全体を出力してください。
"""
user = {"name": "Taro", "age": 20, "city": "Osaka"}
user1 = {"age": 21}
user.update(user1)
print(user)


### 問題5：複数ユーザーの名前の一覧を表示

""" 仕様  
複数のユーザー情報が辞書のリストとして格納されている。全ユーザーの名前だけを表示してください。  

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
for i in range(len(users)):
    print(f"名前:{users[i]["name"]}、年齢:{users[i]["age"]}")
