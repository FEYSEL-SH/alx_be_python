import math
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        return area
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        area = self.radius ** 2 * math.pi
        return area
        
