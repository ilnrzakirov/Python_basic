import os

def gen_files_path(find_catalog: str, catalog = os.path.abspath(os.sep)):
    for path in os.listdir(catalog):
        abs_path = catalog +  "".join(path) + os.sep
        if os.path.isfile(abs_path):
            print(abs_path)
            continue
        else:
            if path == find_catalog:
                print(abs_path)
                return abs_path
            else:
                print(abs_path)
                try:
                    gen_files_path(find_catalog, catalog = abs_path)
                except (PermissionError, NotADirectoryError):
                    print("Пропускаем")

path_list = ["Users", "Ilnur", "PycharmProjects", "python_basic", "module26"]

gen_files_path("04_hof_seq", catalog = os.path.abspath(os.sep) + os.sep.join(path_list) + os.sep )
