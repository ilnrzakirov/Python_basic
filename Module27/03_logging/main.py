import datetime

from typing import Any, Callable

import functools

def logging(func: Callable)-> Callable:
    """
    Декаратор логирующий входящую функцию
    :param func: Callable
    :return: Callable
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs)-> Any:
        print(f"\n Вызываемая функция {func.__name__} \n Документация: \n {func.__doc__}")
             # , предлагаю открывать файл, только если ошибка.
            # , при открытии файла, стоит открывать его с определённой кодировкой. Какой? =)
        try:
            result = func(*args, **kwargs)
            return result
        except (TypeError, ValueError) as err:
            with open("function_errors.log", "a", encoding="UTF-8") as log_file:
                log_file.write(f"Функция: {func.__name__}, Дата и время: {datetime.datetime.now()} Ошибка: {err}")
    return wrapper

@logging
def square(num: int)-> int:
    """
    Функция возвращающая квадрат числа
    :param num: int
    :return: int
    """
    return num ** 2

square("f")