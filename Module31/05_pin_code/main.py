import itertools

numbers = '0123456789'

for paswords in itertools.combinations_with_replacement(numbers, 4):
    print(paswords)