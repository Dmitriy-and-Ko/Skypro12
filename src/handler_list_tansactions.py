import re


def get_list_with_request_string(list_transactions: list, request_string: str) -> list:
    """Функция, принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""
    function_list = list()
    pattern = re.compile(request_string)
    for element in list_transactions:
        if element.get('description') and pattern.search(element['description']):
            function_list.append(element)
    return function_list

