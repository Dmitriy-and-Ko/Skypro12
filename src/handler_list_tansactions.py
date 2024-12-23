import re

def get_list_with_request_string(list_transactions: list, request_string: str) -> list:
    """Функция, принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""
    function_list = list()
    for elment in list_transactions:
        if request_string in elment['description']:
            function_list.append(elment)
    return function_list