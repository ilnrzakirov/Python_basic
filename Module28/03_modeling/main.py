import math


class Square:
    def __init__(self, length: float):
        self.length = length

    def perimeter(self) -> float:
        p = 4 * self.length
        return p

    def square(self) -> float:
        s = self.length ** 2
        return s

#    @property
#    def length(self) -> float:
#        return self.length

#    @length.setter
#    def length(self, length: float) -> None:
#        self.length = length


class FigureSquareMixin:
    @classmethod
    def square_figure(cls, figure_list: list) -> float:
        s = 0
        for figure in figure_list:
            s += figure.square()
        return s


class Triangle:
    def __init__(self, length: float, h: float):
        self.length = length
        self.h = h

    def perimeter(self) -> float:
        a = math.sqrt((1 * self.length ** 2) + self.h ** 2)
        p = self.length + a ** 2
        return p

    def square(self) -> float:
        s = 0.5 * self.length * self.h
        return s


    # TODO таким образом и метод класса и аргумент имеют одинаковое название => length.
    #  Стоит добавить к названию аргумента "_" =)
#    @property
#    def length(self):
#        return self.length

#    @length.setter
#    def length(self, length)-> None:
#        self.length = length


class Pyramid(Triangle, Square, FigureSquareMixin):
    # , предлагаю для расчёта площади каждой фигуры использовать класс Mixin =)
    def __init__(self, length: float, h: float):
        super().__init__(length, h)
        self.element_pyramid = [Triangle(length, h) for _ in range(4)]
        self.element_pyramid.append(Square(length))


class Cube(Square, FigureSquareMixin):
    def __init__(self, length: float):
        super().__init__(length)
        self.element_cube = [Square(length) for _ in range(6)]


p = Pyramid(5,5)
print(p.square_figure(p.element_pyramid))
c = Cube(5)
print(c.square_figure(c.element_cube))
