class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(f"幅: {self.width}")
        print(f"高さ: {self.height}")

    def area(self):
        area = self.width * self.height
        return area
    
    def perimeter(self):
       perimeter = (self.width + self.height) * 2
       return perimeter 
    
rect = Rectangle(5, 3)
print(f"面積: {rect.area()}")
print(f"周囲長: {rect.perimeter()}")
"""
幅: 5
高さ: 3
面積: 15
周囲長: 16
"""