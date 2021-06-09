from collections.abc import Callable
import functools


# , пожалуйста, обратите внимание, арги и кварги в этом месте получились лишними.
#  Стоит добавить ещё одну "обёртку" для аргов и кваргов. А в эту функцию передавать декоратор
def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    def decorator_arg(*args, **kwargs):
        def wrapper(func: Callable):
            print(f"Приведенные арги и кварки в декоратор: {args}, {kwargs}")
            return decorator(func, *args, **kwargs)

        return wrapper

    return decorator_arg


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# зачёт!
