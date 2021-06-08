import datetime
import time
from collections.abc import Callable
import functools
from datetime import datetime

def timer(func: Callable, cls, format) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        date_time = datetime.now().strftime(format)
        print(f'Запускается {cls}.{func.__name__}. Дата и время запуска {date_time}')
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Завершение работы {func.__name__}, время работы {end - start}")
        return result
    return wrapper

def log_methods(format: str) -> Callable:
    date_sym = "bdYHMS"
    date_format = "".join(f"%{x}" if x in date_sym else f"{x}" for x in format)
    print(date_format)
    @functools.wraps(timer)
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith("__") is False:
                curr_method = getattr(cls, i_method)
                decorate_method = timer(func=curr_method, cls=cls.__name__, format=date_format)
                setattr(cls, i_method, decorate_method)
                return cls
    return decorate




@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("Тут меотод test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()