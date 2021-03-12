def calculating_math_func(data, fact_dict={0 : 1}):
    result = 1
    if data in fact_dict:
        result = fact_dict[data]
    else:
        for index in range(1, data + 1):
            result *= index
    fact_dict[data] = result
    result /= data ** 3
    result = result ** 10
    return result

# TODO оптимизировать функцию

print(calculating_math_func(8))