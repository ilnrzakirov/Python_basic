import functools
from collections.abc import Callable


def check_permission(user: str) -> Callable:
    def decarator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper():
            # TODO, в данном случае, права будут только у админа.
            #  Предлагаю ориентироваться на наличие пользователя в списке user_permissions.
            if user == "admin":
                func()
            else:
                print(f"У пользователя {user} недостаточно прав, что бы вызвать функцию {func.__name__}  ")
        return wrapper
    return decarator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
