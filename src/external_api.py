import os
import json
from json import JSONDecodeError, dumps
import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction: dict[str, float]) -> str:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""

    path1 = os.getcwd()
    path2 = '.env'
    joined_path = os.path.join(path1[:-3], path2)

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        to_convert = "RUB"
        from_convert = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_convert}&from={from_convert}&amount={amount}"

        payload = {}
        load_dotenv(joined_path)
        API_KEY = os.getenv('API-KEY')

        headers = {
            "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        # status_code = response.status_code
        result = response.text
        func_result = result[-16:-3]
        # if status_code == 200:
        return func_result
        # else:
        #     return f"Транзакция прошла с ошибкой {status_code}"


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
