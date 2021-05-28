from typing import Callable, Any
import functools

def debug(func: Callable)-> Callable:
    """
    Функция дебагер
    :param func: Callable
    :return: Callable
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs)-> Any:
        # TODO, предлагаю попробовать создать списки из кваргов и аргов
        #  и выводить при помощи именно их =) Таким образом, сделаем вывод более дружелюбным.
        if args and not kwargs:
            print(f"Вызывается: {func.__name__} {args}")
        else:
            print(f"Вызывается: {func.__name__} {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} вернула: {result}")
        print(f"{result} \n")

    return wrapper


@debug
def greeting(name, age=None)-> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)