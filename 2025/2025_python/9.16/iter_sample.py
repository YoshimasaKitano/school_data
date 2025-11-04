### iter_sample.py
colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)

print(colors)

"""
red
blue
green
yellow
['red', 'blue', 'green', 'yellow']
"""

## イテレーターを作る iter()
iter_colors = iter(colors)

print(type(iter_colors)) ### <class 'list_iterator'>

print(next(iter_colors)) ### red
print(next(iter_colors)) ### blue
print(next(iter_colors)) ### green
print(next(iter_colors)) ### yellow

# print(next(iter_colors)) ### StopIteration: エラー