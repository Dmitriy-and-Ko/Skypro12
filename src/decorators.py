import os
from functools import wraps

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data", "log_scripts.txt")
# def log(filename):
#     def user_decor(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             result = func(*args, **kwargs)
#             try:
#                 if filename is not None:
#                     with open("log_scripts")
file = open(PATH_TO_FILE, 'r')
print(file)