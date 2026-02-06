### person.py
"""
カプセル化(隠ぺい)：インスタンス変数を非公開にする
public：公開
protected：非公開を明示 → _name「触らないで」
private：非公開 → __name「完全に隠したい」マングリング
"""
class Person:
    def __init__(self):
        self.__name = "" # 属性を隠ぺい化

    ## 同じクラス内であれば取得できる
    # 属性: インスタンス変数の値を取得する ゲッター
    def getter(self):
        return self.__name
    
    # 属性: インスタンス変数に値をセットする セッター
    def setter(self, name):
        self.__name = name
    
    
p1 = Person()
# print(p1.__name) ### エラー

# セッターを使って値をセット
p1.setter("takekuni")


# ゲッターを使って値を取得
name = p1.getter()
print(name) ### takekuni

#どうしても見たい場合
print(p1._Person__name) ### takekuni