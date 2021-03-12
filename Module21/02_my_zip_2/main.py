def max_len (object1, object2):
    return min(len(object1), len(object2))

def generator (object1, object2):
    result = ((object1[i_elem], object2[i_elem]) for i_elem in range (max_len(object1,object2)))
    return result

#def print_res_gen (object):


lst = [3, 5, 6, 1, 5]
tpl = (5, 4 , 3, 7)
str = "avddgddfd"


result = generator(lst, str)
#print_res_gen(result)
print(result)
for sym in result:
    print(sym)