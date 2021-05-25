import modulefinder
import os


def gen_files_path(find_catalog: str, catalog):
    for path in os.listdir(catalog):
        # , возможно, конкатенация и join получились лишними.
        #  Предлагаю работать сразу с os.path.join
        abs_path = os.path.join(catalog, path) + os.sep
        print(abs_path)
        if os.path.isfile(abs_path):
            # , print лишний, функция должна возвращать элемент.
            # , если файл, то возвращаем
            yield abs_path
            # , Предлагаю убрать continue, т.к. ничего не пропускает.
        elif os.path.isdir(abs_path):  # , блок else лишний. Стоит проверять, является ли директорией.
            # , если директория, то получаем её базовое название и сравниваем с find_catalog.
            #  Если совпало, в таком случае работу генератора стоит завершить =)
            #  Если не совпало запускаем цикл по нашей функции gen_files_path, т.к. она итерируемая =)
            print(os.path.basename(abs_path))
            # TODO, дело в том, что basename у abs_path это путь до папки C:\Users...
            #  а find_catalog это сама папка => 03_files_path =)
            if os.path.basename(abs_path) == find_catalog:
                # , print лишний
                return abs_path  # , только yield. =)
            else:
                for path in gen_files_path(find_catalog, abs_path):
                    yield path
                    # , в этом месте стоит возвращать path при помощи yield


# , предлагаю запрашивать путь сразу целиком, не разделяя на папки.
path_folder = input("Введите путь для поиска: ")
find = input("Введите папку для поиска")
for item in gen_files_path(find_catalog=find, catalog=path_folder):
    print(item)

# TODO Введите путь для поиска: C:\...\ilnur_zakirov\python_basic
#  Введите папку для поиска 03_files_path
#  Пока что программа не выводит ничего =) Предлагаю добавить вывод возвратов Генератора и проверить.
