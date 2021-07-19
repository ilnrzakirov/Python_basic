import itertools

numbers = '0123456789'

for paswords in itertools.combinations_with_replacement(numbers, 4):
    print(paswords)
# TODO Пожалуйста, обратите внимание, вариант (9, 9, 9, 8) тоже должен быть доступен.
#  всего должно получиться 10000 вариантов. Предлагаю попробовать найти функцию модуля itertools,
#  при помощи которой мы сможем учесть все варианты. =)
