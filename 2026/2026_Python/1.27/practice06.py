from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (self.radius ** 2) * 3.14
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return float(self.width * self.height)
    
    def perimeter(self):
        return float(2 * (self.width + self.height))

shapes = []

shapes.append(Circle(3))
shapes.append(Rectangle(4, 5))
shapes.append(Circle(1))
shapes.append(Rectangle(2, 6))

for shape in shapes:
    if shape.area() / 3.14 == 0:
        print(f"Circle → 面積: {shape.area():.2f}, 周囲長: {shape.perimeter():.2f}")
    else:
        print(f"Rectangle → 面積: {shape.area():.2f}, 周囲長: {shape.perimeter():.2f}")