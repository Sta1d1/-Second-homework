from Figure import Figure
import math

class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Значения должны быть больше 0")
        self.radius = radius
    
    def get_area(self):
        return (self.radius * math.pi) ** 2
    
    def get_perimeter(self):
        return 2 * self.radius * math.pi
