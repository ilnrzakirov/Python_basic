from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декаратор спрашивающий самочувствие пользователя =)
    :return: Callable
    """

    def wrapper(*args, **kwargs) -> Any:  # , функция должна принимать на вход арги и кварги и передавать их в func =)
        input("Как дела: ")
        print("А у меня не очень! Ладно, держи свою функцию")
        return func(*args, **kwargs)

    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()

# зачёт!
