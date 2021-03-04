def great_tuple (element1, element2):
    return element1, element2

my_string = "abcd"
my_tuple = ("d", 20, 30, 40)

if len(my_string) <= len(my_tuple):
    for i_item, item in enumerate(my_string):
        print(great_tuple(item, my_tuple[i_item]))
else:
    for i_item, item in enumerate(my_tuple):
        print(great_tuple(item, my_string[i_item]))
