### user_sample.py
"""
ユーザーの概念を表すクラス
・名前、年齢、人数を持つ
・大人、子供
"""
class User:
    # クラス変数:共通
    user_count = 0 # 人数

    # 初期化:属性を定義
    """インスタンスメソッド"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

        User.user_count += 1

    def introduce(self):
        return f"私の名前は{self.name}です。{self.age}歳です。"

    """クラスメソッド"""
    @classmethod
    def create_child(cls, name):
        return cls(name, age = 10)

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    """スタティックメソッド"""
    @staticmethod
    def is_adult(age):
        return age >= 18 # 18以上の場合True

# 動作確認
# インスタンスの生成
user1 = User("太郎", 20)

# インスタンスメソッドを呼び出し
print(user1.introduce()) ### 私の名前は太郎です。20歳です。

# クラスメソッドの呼び出し
user2 = User.create_child("花子")
print(user2.introduce()) ### 私の名前は花子です。10歳です。

print(f"ユーザー数:{User.get_user_count()}") ### ユーザー数:2

# スタティックメソッド
print(f"{user1.name}は成人か？:{User.is_adult(user1.age)}") ### 太郎は成人か？:True
print(f"{user2.name}は成人か？:{User.is_adult(user2.age)}") ### 花子は成人か？:False