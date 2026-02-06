### practice07.py
"""
タスクの追加・削除・状態変更・一覧表示を行う
タスクを表すTask クラス
複数のタスクを管理する TaskManager クラス
"""
# Task:個々のタスクを表現するデータモデル
class Task:

    ## 初期化設定
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.done = False

    ## タスクを完了状態（done=True）に変更する
    def mark_done(self):
        self.done = True

    ## タスク内容を文字列として整形して返す
    def __str__(self):
        status = "✔ 完了" if self.done else "✗ 未完了"
        return f"[{status}] : {self.title} (優先度: {self.priority})"


# TaskManager:複数のタスクを保持し、追加・削除・一覧表示を行う管理クラス
class TaskManager:

    ## 初期化設定 
    def __init__(self):
        self.tasks = []

    ## Task オブジェクトをリストに追加するメソッド
    def add_task(self, task):
        self.tasks.append(task)

    ## タイトルが一致するタスクを削除するメソッド
    def remave_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    ## 優先度の高い順にタスクを並べて表示するメソッド
    def list_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda t: t.priority, reverse=True)

        for task in sorted_tasks:
            print(task)


# 動作確認
## インスタンスの生成
manager = TaskManager()

## タスクの追加
manager.add_task(Task("買い物に行く",2))
manager.add_task(Task("レポートを書く",5))
manager.add_task(Task("部屋を掃除する",3))

## 完了処理
manager.tasks[1].mark_done()

## 一覧表示
print("=== タスク一覧 ===")
manager.list_tasks()

## タスクの削除
manager.remave_task("買い物に行く")

## 削除後の一覧表示
print("=== 削除後のタスク一覧 === ")
manager.list_tasks()    

