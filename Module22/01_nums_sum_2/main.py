input_file = open("numbers.txt", "r")
res_num = 0

for i_line in input_file:
    for i_elem in i_line:
        if i_elem != " " and i_elem != "\n":
            res_num += int(i_elem)

answer = open("answer.txt", "w")
answer.write(str(res_num))

input_file.close()
answer.close()

# зачёт!
