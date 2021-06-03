from abc import ABC, abstractmethod
import math

class MyMath(ABC):
    """
    Абстрактный класс
    """
    @classmethod
    def len_circle(cls, r: float)-> float:
        """
        Метод для нахождения длины окружности
        :param r: float
        :return: float
        """
        return 2 * math.pi * r

    @classmethod
    def square_circle(cls, r: float)-> float:
        """
        Метод для нахождения площади круга
        :param r: float
        :return: float
        """
        return math.pi * r ** 2

    @classmethod
    def volume_cube(cls, length: float)-> float:
        """
        Метод для нахождения объема куба
        :param length: float
        :return: float
        """
        return length ** 3

    @classmethod
    def surface_area(cls, r: float)-> float:
        """
        Метод для нахождения площади поверхности сферы
        :param r: float
        :return: float
        """
        return 4 * math.pi * r


res1 = MyMath.len_circle(r=5)
res2 = MyMath.square_circle(r=6)
print(res1)
print(res2)

# зачёт!