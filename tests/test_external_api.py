import os
from unittest.mock import patch


import requests
from unittest import mock
from dotenv import load_dotenv
from src.external_api import get_transaction_amount

@patch('requests.request')
def test_get_transaction_amount_for_RUB_currency(mock_get):
    mock_get.return_value = {"operationAmount":{"amount": 1, "currency": {"code": "RUB"}}}
    assert get_transaction_amount({"operationAmount":{"amount": 1, "currency": {"code": "RUB"}}}) == 1


@patch('requests.get')
def test_get_transaction_amount_for_USD_currency(mock_get, to_convert="RUB", from_convert="USD", amount=1, payload={}):
    mock_get.return_value = 'und in reques'
    assert get_transaction_amount({"operationAmount":{"amount": 1, "currency": {"code": "USD"}}}) == 'und in reques'
    path1 = os.getcwd()
    path2 = '.env'
    joined_path = os.path.join(path1[:-3], path2)
    load_dotenv(joined_path)
    API_KEY = os.getenv('API-KEY')
    headers = {
        "apikey": API_KEY
    }
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_convert}&from={from_convert}&amount={amount}"
    mock_get.assert_called_once_with("GET", url, headers=headers, data=payload)

