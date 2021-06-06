from collections.abc import Callable
import functools

# , пока то, лишний импорт

app = dict()


# , предлагаю создать пустой словарь и заполнять его внутри декоратора.
#  Исходя из нашего примера, ключом будет "//", а значением наша функция.


def callback(command: str) -> Callable:
    def decorate(func: Callable) -> Callable:
        app[command] = func

        @functools.wraps(func)
        def wrapper():
            return func()

        return wrapper

    return decorate


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачёт!
