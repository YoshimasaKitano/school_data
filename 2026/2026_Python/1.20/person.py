### person.py
"""
カプセル化(隠ぺい)：インスタンス変数を非公開にする
public：公開
protected：非公開を明示 → _name「触らないで」
private：非公開 → __name「完全に隠したい」マングリング
"""
class Person:
    def __init__(self, name):
        self.__name = name
    
p1 = Person("takekuni")
# print(p1.__name) ### エラー

#どうしても見たい場合
print(p1._Person__name) ### takekuni