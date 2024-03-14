from src.Figure import Figure
import math

class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Значения должны быть больше 0")
        self.radius = radius
    
    @property
    def get_area(self):
        return (self.radius ** 2) * math.pi
    
    @property
    def get_perimeter(self):
        return 2 * self.radius * math.pi

