import os


def gen_files_path(find_catalog: str, catalog=os.path.abspath(os.sep)):
    for path in os.listdir(catalog):
        # , возможно, конкатенация и join получились лишними.
        #  Предлагаю работать сразу с os.path.join
        abs_path = os.path.join(path) + os.sep
        if os.path.isfile(abs_path):
            # , print лишний, функция должна возвращать элемент.
            # , если файл, то возвращаем
            yield abs_path
            # , Предлагаю убрать continue, т.к. ничего не пропускает.
        elif os.path.isdir(abs_path):  # , блок else лишний. Стоит проверять, является ли директорией.
            directory = os.path.basename(abs_path)
            # , если директория, то получаем её базовое название и сравниваем с find_catalog.
            #  Если совпало, в таком случае работу генератора стоит завершить =)
            #  Если не совпало запускаем цикл по нашей функции gen_files_path, т.к. она итерируемая =)
            if directory == find_catalog:
                # , print лишний
                return abs_path  # , только yield. =)
            else:
                for path in gen_files_path(abs_path):
                    yield path
                    # , в этом месте стоит возвращать path при помощи yield


#                    directory = os.path.basename(path)
#                    if directory == find_catalog:
#                        return abs_path


# , предлагаю запрашивать путь сразу целиком, не разделяя на папки.
# path_list = ["Users", "Ilnur", "PycharmProjects", "python_basic", "module26"]
path_folder = input("Введите путь для поиска: ")
find = input("Введите папку для поиска")
# gen_files_path("04_hof_seq", catalog=os.path.abspath(os.sep) + os.sep.join(path_list) + os.sep)
gen_files_path(find, path_folder)

# TODO Введите путь для поиска: C:\...\ilnur_zakirov\python_basic
#  Введите папку для поиска 03_files_path
#  Пока что программа не выводит ничего =) Предлагаю добавить вывод возвратов Генератора и проверить.
