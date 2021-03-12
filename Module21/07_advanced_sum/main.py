def summ (object, result= 0):
    for item in object:
        if isinstance(item, list):
            summ(item, result)
        else:
            result += item
    return result

# Обьясните пожалуйста, почему после возврата result = 11 с рекурсии, функция не обращает на это внимание, а
# пользуется предыдущим значением = 6. И получается так, что недосчитывает значение с подсписков.

my_list = [1, 2, 3, [5], 8, [1, 2]]
print(summ(my_list))