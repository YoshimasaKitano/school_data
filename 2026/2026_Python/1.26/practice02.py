class Counter:
    def __init__(self, count = 0):
        self.count = count
    
    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0
        print(f"リセット後の値: {self.count}")

counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(f"現在の値: {counter.count}")
counter.reset()
"""
現在の値: 3
リセット後の値: 0
"""