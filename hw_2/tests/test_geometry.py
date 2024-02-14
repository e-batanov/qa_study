from hw_2.src.Triangle import Triangle
from hw_2.src.Square import Square
from hw_2.src.Circle import Circle
from hw_2.src.Rectangle import Rectangle
from hw_2.src.Figure import Figure
import pytest
from math import pi


@pytest.mark.parametrize("figure_class, args, expected_area, expected_perimeter", [
    (Triangle, (3, 4, 5), 6, 12),
    (Square, (4,), 16, 16),
    (Rectangle, (4, 5), 20, 18),
    (Circle, (5,), pi * 25, 2 * pi * 5),
])
def test_figures(figure_class, args, expected_area, expected_perimeter):
    figure = figure_class(*args)
    assert figure.area() == expected_area
    assert figure.perimeter() == expected_perimeter
    with pytest.raises(ValueError):
        figure.add_area(10)


def test_figure_raises_type_error():
    with pytest.raises(TypeError):
        f = Figure(name='Figure')

