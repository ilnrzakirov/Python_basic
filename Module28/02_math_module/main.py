from abc import ABC, abstractmethod
import math

class MyMath(ABC):
    @classmethod
    def len_circle(cls, r: float)-> float:
        return 2 * math.pi * r

    @classmethod
    def square_circle(cls, r: float)-> float:
        return math.pi * r ** 2

    @classmethod
    def volume_cube(cls, length: float)-> float:
        return length ** 3

    @classmethod
    def surface_area(cls, r: float)-> float:
        return 4 * math.pi * r


res1 = MyMath.len_circle(r=5)
res2 = MyMath.square_circle(r=6)
print(res1)
print(res2)