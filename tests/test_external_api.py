import os
from unittest.mock import patch
from flask import Flask
import pytest
import requests
from unittest import mock
from dotenv import load_dotenv
from src.external_api import get_transaction_amount


@patch("requests.request")
def test_get_transaction_amount_for_RUB_currency(mock_get):
    mock_get.return_value = {"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}
    assert get_transaction_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1


@patch("requests.request")
def test_get_transaction_amount_for_USD_currency(mock_get):
    mock_get.return_value.text = '{"result": 1}'
    assert get_transaction_amount({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}) == 1
    path1 = os.getcwd()
    path2 = ".env"
    joined_path = os.path.join(path1[:-3], path2)
    load_dotenv(joined_path)
    API_KEY = os.getenv("API-KEY")
    headers = {"apikey": API_KEY}
    url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    mock_get.assert_called_with("GET", url, headers=headers, data={})
