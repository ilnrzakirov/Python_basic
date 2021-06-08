from collections.abc import Callable
import functools

def decorator_with_args_for_any_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Приведенные арги и кварки в декоратор: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(_func: Callable, *args, **kwargs):
    def decorate(func, *args, **kwargs):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate



@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)