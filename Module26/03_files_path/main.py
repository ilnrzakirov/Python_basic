import os

def gen_files_path(find_catalog: str, catalog = os.path.abspath(os.sep)):
    for path in os.walk(catalog):
        yield path
        if find_catalog in path:
            return




directory = gen_files_path(os.getcwd())
for item in directory:
    print(item)
