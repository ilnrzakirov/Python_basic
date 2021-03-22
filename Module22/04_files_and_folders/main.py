import os


def struct_dir(path, file_count=0, all_size=0):
    for i_elem in os.listdir(path):
        path_fld = os.path.join(path, i_elem)
        if os.path.isfile(path_fld):
            file_count += 1
            all_size += os.path.getsize(path_fld) / 1024
        else:
            file_count, all_size = struct_dir(path_fld, file_count, all_size)
    return file_count, all_size


path = os.path.abspath(os.path.join("..", "..", "Module14"))
print(path)
print("Количество подкаталогов: ", len(os.listdir(path)))
file_count, all_size = struct_dir(path)
print("Количество файлов: {} \nРазмер каталога в(Кб): {}".format(file_count, all_size))

# зачёт!
