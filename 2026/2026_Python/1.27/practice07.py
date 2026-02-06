class Task:
    def __init__(self, title, priority, done = False):
        self.title = title
        self.priority = priority
        self.done = done
    
    def mark_done(self):
        self.done = True

    def __str__(self):
        if self.done == True:
                return f"[✔ 完了]{self.title}(優先度: {self.priority})"
        else:
                return f"[✗ 未完了]{self.title}(優先度: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    # @classmethod
    def add_task(self, task):
        self.tasks.append(task)
    
    # @classmethod
    def remove_task(self, title):
        for task in self.tasks:
            if title == task[self.title]:
                self.tasks.remove(task)

        print("=== 削除後のタスク⼀覧 ===")
        for task in self.tasks:
            if task[self.done] == True:
                print(f"[✔ 完了]{task[self.title]}(優先度: {task[self.priority]})")
            else:
                print(f"[✗ 未完了]{task[self.title]}(優先度: {task[self.priority]})")
    
    # @classmethod
    def list_tasks(self):
        sorted(self.tasks, key=lambda t: t.priority, reverse=True)
        print("=== タスク⼀覧 ===")
        for task in self.tasks:
            print(task)

task1 = Task("買い物に行く", 2)
task2 = Task("レポートを書く", 5)
task3 = Task("部屋を掃除する", 3)

manage = TaskManager()

manage.add_task(task1)
manage.add_task(task2)
manage.add_task(task3)

task2.mark_done()

manage.list_tasks()

manage.remove_task("買い物に行く")
