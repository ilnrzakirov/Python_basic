from collections.abc import Callable
import functools
from flask import Flask  # TODO, пока то, лишний импорт

app = Flask(__name__)
# TODO, предлагаю создать пустой словарь и заполнять его внутри декоратора.
#  Исходя из нашего примера, ключом будет "//", а значением наша функция.


def callback(command: str) -> Callable:
    def decorate(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper():
            if command == "//":
                example()
        return wrapper
    return decorate


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route(example)
    print('Ответ:', response)
else:
    print('Такого пути нет')
