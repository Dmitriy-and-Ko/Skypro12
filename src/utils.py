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


def get_transaction_amount(transaction: dict[str, float]) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        to_convert = "RUB"
        from_convert = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/currency_data/convert?to={to_convert}&from={from_convert}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "GOaGE3RxnJdtk0E343HyL9luojqmns7H"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.text
        func_result = round(float(result[-16:-3]), 2)
        return func_result


if __name__ == '__main__':
    print(get_transaction_amount({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))


'GOaGE3RxnJdtk0E343HyL9luojqmns7H'