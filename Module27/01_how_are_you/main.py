from typing import Callable, Any


def how_are_you(func: Callable)-> Callable:
    """
    Декаратор спрашивающий самочувствие пользователя =)
    :return: Callable
    """
    def wrapper()-> Any:
        input("Как дела: ")
        print("А у меня не очень! Ладно, держи свою функцию")
        return func()
    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()