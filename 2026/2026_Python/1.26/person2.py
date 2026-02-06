### person2.py
"""
カプセル化(隠ぺい)：インスタンス変数を非公開にする
public：公開
protected：非公開を明示 → _name「触らないで」
private：非公開 → __name「完全に隠したい」マングリング
"""
from tkinter.messagebox import RETRY


class Person:
    def __init__(self):
        self.__name = "" # 属性を隠ぺい化

    ## 同じクラス内であれば取得できる
    # 属性: インスタンス変数の値を取得する ゲッター
    @property
    def name(self):
        return self.__name
    
    # 属性: インスタンス変数に値をセットする セッター
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
    
    
p1 = Person()
# print(p1.__name) ### エラー

# セッタープロパティを使って値をセット
p1.name = "takekuni"
p1.age = 40

# ゲッタープロパティを使って値を取得
print(f"取得した名前:{p1.name}、年齢:{p1.age}歳") ### 取得した名前:takekuni、年齢:40歳

#どうしても見たい場合
print(p1._Person__name) ### takekuni