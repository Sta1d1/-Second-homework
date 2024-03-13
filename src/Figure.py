"""Figure module"""

from abc import ABC, abstractmethod



class Figure(ABC):
    """Figure parent class"""

    def __init__(self, name):
        self.name = name
    @abstractmethod
    def get_area(self):
        """abstraction get_area function"""
        pass
    @abstractmethod
    def get_perimeter(self):
        """abstraction get_perimeter function"""
        pass
    def add_area(self, other_figure):
        """add_area function."""
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужен класс Figure")
        return self.get_area() + other_figure.get_area()
    
