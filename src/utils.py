import os
import json
from json import JSONDecodeError, dumps
import requests

path1 = os.getcwd()
path2 = 'data'
path3 = 'operations.json'
joined_path = os.path.join(path1[:-3], path2, path3)


def get_list_transactions(file_path: str) -> list:
    """Функция возвращает список словарей с данными о финансовых транзакциях, на вход принимает путь к файлу"""
    if file_path == joined_path:
        try:
            with open(joined_path, 'r', encoding='utf-8') as json_file:
                transaction_list = json.load(json_file)
                return transaction_list
        except JSONDecodeError:
            return []
    return []


