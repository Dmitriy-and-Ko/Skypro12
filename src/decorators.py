import os
from functools import wraps

# ROOT_DIR = Path(__file__).parent
# print(ROOT_DIR)
# PATH_TO_FILE = Path(ROOT_DIR, "data", "log_scripts.txt")
PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data", "log_scripts.txt")
def log(filename):
    def user_decor(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename is not None:
                with (open(PATH_TO_FILE, 'a', encoding="utf-8") as file):
                    return file.write(result)
            else:
                return result
        return inner
    return user_decor

# print(PATH_TO_FILE)
# with (open(PATH_TO_FILE, 'a', encoding="utf-8") as file):
#     content = "Учись работать с файлами. \n"
#     file.write(content)
