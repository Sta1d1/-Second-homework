from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Значения должны быть больше 0")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b
    
    @property
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)