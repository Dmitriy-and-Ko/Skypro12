import os
from fileinput import filename
from functools import wraps

# ROOT_DIR = Path(__file__).parent
# print(ROOT_DIR)
# PATH_TO_FILE = Path(ROOT_DIR, "data", "log_scripts.txt")
PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data", "log_scripts.txt")
def log(filename = None):
    def user_decor(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with (open(PATH_TO_FILE, 'a', encoding="utf-8") as file):
                        return file.write(f"Выполнена функция {func.__name__}, результат {result}.\n")
                else:
                    return result
            except Exception as error:
                if filename is not None:
                    with (open(PATH_TO_FILE, 'a', encoding="utf-8") as file):
                        return file.write(f"Выполнена функция {func.__name__}, произошла ошибка {error}, атрибуты фукции {args}, {kwargs}.\n")
                else:
                    return print(f"Выполнена функция {func.__name__}, произошла ошибка {error}, атрибуты фукции {args}, {kwargs}.\n")
        return inner
    return user_decor

# print(PATH_TO_FILE)
# with (open(PATH_TO_FILE, 'a', encoding="utf-8") as file):
#     content = "Учись работать с файлами. \n"
#     file.write(content)
@log()
def sum_two_numbers(a, b):
    return a + b

sum_two_numbers(11, 12)

@log('log_s')
def sum_two_numbers(a, b):
    return a + b

sum_two_numbers("15", "21")

@log("name")
def sum_two_numbers(a, b):
    return a + b

sum_two_numbers("24", 32)

@log()
def sum_two_numbers(a, b):
    return a + b

sum_two_numbers("24", 32)

def sum_two_numbers(a, b):
    return a + b

