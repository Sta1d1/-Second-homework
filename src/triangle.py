from Figure import Figure

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        super().__init__(name="Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self): 
        sp =(self.side1 + self.side2 + self.side3) / 2 
        area =(sp*(sp-self.side1)*(sp-self.side2)*(sp-self.side3)) ** 0.5 
        return area

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

