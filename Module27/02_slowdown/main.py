import time
from typing import Callable, Any
from time import sleep


def how_are_you(func: Callable)-> Callable:
    """
    Декаратор спрашивающий самочувствие пользователя =)
    :return: Callable
    """
    def wrapper(*args, **kwargs)-> Any: # TODO, функция должна принимать на вход арги и кварги и передавать их в func =)
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()