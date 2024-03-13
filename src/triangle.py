from Figure import Figure

class Triangle(Figure):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        side1 = args[0]
        side2 = args[1]
        side3 = args[2]
        if side1 + side2 < side3 or side2 + side3 < side1 or side3 + side1 < side2 or side1 == 0 or side2 == 0 or side3 == 0:
            raise ValueError("Треугольник не может существовать.")
        return instance
    def __init__(self, side1, side2, side3):
        super().__init__(name="Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def get_area(self): 
        sp =(self.side1 + self.side2 + self.side3) / 2 
        area =(sp*(sp-self.side1)*(sp-self.side2)*(sp-self.side3)) ** 0.5 
        return area

    @property
    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

a = Triangle(10,4,5)
print(a.get_area)