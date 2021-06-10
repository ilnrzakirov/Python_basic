import functools

def singleton(cls):
    @functools.wraps(cls)

    def wrapper():

        if hasattr(cls, "init") is False:
            cls.init = cls.__new__
        return cls.init
    return wrapper

# TODO, Возможно, не очень правильная идея опираться на класс init.
#  Если учесть, что всё в python является объектами класса, возможно будет лучше создать аргумент у функции декоратора
#  и присвоить значение объекта класса ему. Помните, как мы создавали аргумент для подсчёта количества вызовов функций
#  в предыдущем уроке?


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)