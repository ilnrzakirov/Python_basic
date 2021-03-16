def calculating_math_func(data, fact_dict={0: 1}):
    result = 1
    # , возможно условный ператор не нужен =).
    #   fact_dict лишний параметр.
    if data in fact_dict:
        result = fact_dict[data]
    else:
        for index in range(1, data + 1):
            result *= index
    fact_dict[data] = result
    result /= data ** 3
    result = result ** 10
    return result


#  оптимизировать функцию

print(calculating_math_func(5))

# зачёт!
