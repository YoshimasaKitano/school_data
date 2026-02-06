### class_summary.py
"""
クラス定義のまとめ
"""
class Sample: # クラス名は頭大文字

    # 初期化メソッド:属性(インスタンス変数)を定義する
    def __init__(self, name):
        self.name = name

    # インスタンスメソッド
    def show_name(self):
        print(self.name)
        Sample.greet() # スタティックメソッドを呼び出す

    # クラスメソッド
    @classmethod
    def create_default(cls):
        return "名無しの権兵衛"

    # スタティックメソッド:クラス内で一時的に使うことが多いメソッド
    @staticmethod
    def greet():
        print("こんにちは！")

# クラスメソッドの呼び出し
default = Sample.create_default()
print(default) ### 名無しの権兵衛

# インスタンスを生成して、インスタンスメソッドを呼び出す
obj = Sample("竹國")
obj.show_name() ### 竹國
