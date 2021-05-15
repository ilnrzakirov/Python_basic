import os


def gen_files_path(find_catalog: str, catalog=os.path.abspath(os.sep)):
    for path in os.listdir(catalog):
        # TODO, возможно, конкатенация и join получились лишними.
        #  Предлагаю работать сразу с os.path.join
        abs_path = catalog + "".join(path) + os.sep
        if os.path.isfile(abs_path):
            print(abs_path)
            # TODO, если файл, то возвращаем
            continue  # TODO, Предлагаю убрать continue, т.к. ничего не пропускает.
        else:
            # TODo, если директория, то получаем её базовое название и сравниваем с find_catalog.
            #  Если совпало, в таком случае работу генератора стоит завершить =)
            #  Если не совпало запускаем цикл по нашей функции gen_files_path, т.к. она итерируемая =)
            if path == find_catalog:
                print(abs_path)
                yield abs_path  # , только yield. =)
            else:
                print(abs_path)
                try:
                    gen_files_path(find_catalog, catalog=abs_path)
                except (PermissionError, NotADirectoryError):
                    print("Пропускаем")


# , предлагаю запрашивать путь сразу целиком, не разделяя на папки.
# path_list = ["Users", "Ilnur", "PycharmProjects", "python_basic", "module26"]
path_folder = input("Введите путь для поиска: ")
find = input("Введите папку для поиска")
# gen_files_path("04_hof_seq", catalog=os.path.abspath(os.sep) + os.sep.join(path_list) + os.sep)
gen_files_path(find, path_folder)
