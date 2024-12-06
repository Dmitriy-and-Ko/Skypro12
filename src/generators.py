from typing import Union


def filter_by_currency(transaction_list: Union[list, dict], currency: str) -> Union[list, dict]:
    """Функция, принимающая список транзакций, и возвращающая итератор, где валюта операции соответствует заданной"""
    filtred_expression = (
        transaction
        for transaction in transaction_list
        if transaction["operationAmount"]["currency"]["name"] == currency
    )
    return filtred_expression


def transaction_descriptions(list_of_transaction: Union[list, dict]) -> None:
    """Генератор, принимающий список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    try:
        list_of_transaction == list()
    except RuntimeError or StopIteration:
        print("Отсутствуют данные для транзакции")
    else:
        for transaction in list_of_transaction:
            print(f"Id транзакции {transaction['id']}")
            yield transaction["description"]


def card_number_generator(low_limit: int, upper_limit: int) -> int:
    """Генератор банковских карт. Выдаёт номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ где Х - цифра"""
    numbers_generate = (x for x in range(low_limit, upper_limit))
    for number in numbers_generate:
        number = str(number).zfill(16)
        yield f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
