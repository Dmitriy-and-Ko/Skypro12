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


def count_transaction_category(list_transactions: list, list_category: list) -> dict:
    '''Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.'''
    result = {}
    for element in list_transactions:
      for value in element.values():
        if value in list_category:
          result[value] = result.get(value, 0) + 1
    return result

