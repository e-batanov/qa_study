from hw_2.src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4
