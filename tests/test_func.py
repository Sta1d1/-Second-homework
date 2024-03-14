import pytest
import math
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle

# RECTANGLE TESTS
def test_rectangle_area_good():
    rec = Rectangle(3,5)
    assert rec.get_area == 15

def test_rectangle_perimeter_good():
    rec = Rectangle(3,5)
    assert rec.get_perimeter == 16

@pytest.mark.parametrize("first_value, second_value", [(-3, 5), (3, 0), (0, -5)])
def test_rectangle_negative_all_value(first_value, second_value):
    with pytest.raises(ValueError) as excinfo:
        rec = Rectangle(first_value,second_value)
        rec.get_area
        assert excinfo.group_contains(ValueError)


# SQUARE TESTS
def test_square_area_good():
    sqr = Square(3)
    assert sqr.get_area == 9

def test_square_perimeter_good():
    sqr = Square(3)
    assert sqr.get_perimeter == 12

@pytest.mark.parametrize("value", [(0), (-1)])
def test_square_negative_all_value(value):
    with pytest.raises(ValueError) as excinfo:
        sqr = Square(value)
        sqr.get_area
        assert excinfo.group_contains(ValueError)


# TRIANGLE TESTS
@pytest.mark.parametrize("v1, v2, v3, res", [(3,4,5,6)])
def test_triangle_area_good(v1, v2, v3, res):
    trg = Triangle(v1, v2, v3)
    assert trg.get_area == res

@pytest.mark.parametrize("v1, v2, v3, res", [(3,4,5,12), (1,2,3,6), (5,3,3,11)])
def test_triangle_perimeter_good(v1, v2, v3, res):
    trg = Triangle(v1, v2, v3)
    assert trg.get_perimeter == res

@pytest.mark.parametrize("v1, v2, v3", [(1,2,5), (6,3,2), (1,7,2), (0,1,2),(-1,0,3),(3,0,-1),(5,-1,3)])
def test_triangle_negative_all_value(v1, v2, v3):
    with pytest.raises(ValueError) as excinfo:
        trg = Triangle(v1, v2, v3)
        trg.get_area
        assert excinfo.group_contains(ValueError)


# CIRCLE TEST
@pytest.mark.parametrize("value", [(1), (2), (3), (4), (5)])
def test_circle_area_good(value):
    cir = Circle(value)
    assert cir.get_area == (value ** 2) * math.pi

@pytest.mark.parametrize("value", [(1), (2), (3), (4), (5)])
def test_circle_perimeter_good(value):
    cir = Circle(value)
    assert cir.get_perimeter == 2 * value * math.pi

@pytest.mark.parametrize("value", [(0), (-1)])
def test_circle_negative_all_value(value):
    with pytest.raises(ValueError) as excinfo:
        cir = Circle(value)
        cir.get_area
        assert excinfo.group_contains(ValueError)

