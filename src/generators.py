from typing import Union
def filter_by_currency(transaction_list: Union[list, dict], currency: str)->Union[list, dict]:
    """Функция, принимающая список транзакций, и возвращающая итератор, где валюта операции соответствует заданной"""
    filtred_expression = filter(lambda x: x["currency"]["code"] == currency, transaction_list)
    return filtred_expression


def transaction_descriptions(list_of_transaction: Union[list, dict])->None:
    """Генератор, принимающий список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in list_of_transaction:
        if transaction["state"] == "EXECUTED":
            print(f"Id транзакции {transaction['id']}")
            yield transaction["description"]


