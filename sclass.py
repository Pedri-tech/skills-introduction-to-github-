


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle:
    def __init__(self, color, is_filled, radius):
        Shape.__init__(color, is_filled)
        self.radius = radius

class Square:
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

class Triangle:
    def __init__(self, color, is_filled, base, height):
        Shape.__init__(color, is_filled)
        self.base = base
        self.height = height

circle = Circle(color = "red", is_filled = True, radius = 5)

print(circle.color)