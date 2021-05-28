from typing import Any, Callable

import functools


def counter(func: Callable) -> Callable:
    """
    Декартор считающий количество вызывов функции
    :param func: Callable
    :return: Callable
    """
    functools.wraps(func)
    func.count = 0

    def wrapper(*args, **kwargs) -> Any:
        func.count += 1
        print(f"Фунцкия вызывалась {func.count} раз")
        return func(*args, **kwargs)

    return wrapper


@counter
def square(num: int) -> int:
    """
    Функция возвращающая квадрат числа
    :param num: int
    :return: int
    """
    return num ** 2


square(2)
square(2)
square(2)
square(2)
square(2)
square(2)

# зачёт!
