from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Figure import Figure
import pytest
from math import pi


def test_figure():
    with pytest.raises(TypeError):
        f = Figure(name='Figure')


def test_triangle():
    t = Triangle(3, 4, 5)
    assert t.area() == 6
    assert t.perimeter() == 12
    with pytest.raises(ValueError):
        t.add_area(10)


def test_square():
    s = Square(4)
    assert s.area() == 16
    assert s.perimeter() == 16
    with pytest.raises(ValueError):
        s.add_area(10)


def test_rectangle():
    r = Rectangle(4, 5)
    assert r.area() == 20
    assert r.perimeter() == 18
    with pytest.raises(ValueError):
        r.add_area(10)


def test_circle():
    c = Circle(5)
    assert c.area() == pi * 25
    assert c.perimeter() == 2 * pi * 5
    with pytest.raises(ValueError):
        c.add_area(10)

