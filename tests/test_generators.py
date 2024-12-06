import pytest
from src.generators import card_number_generator, transaction_descriptions, filter_by_currency
from tests.test_transactions import transactions


def test_card_number_generator():
    generator = card_number_generator(34562812, 34562816)
    assert next(generator) == "0000 0000 3456 2812"
    assert next(generator) == "0000 0000 3456 2813"
    assert next(generator) == "0000 0000 3456 2814"
    assert next(generator) == "0000 0000 3456 2815"


def test_card_number_generator_with_low_limit():
    generator = card_number_generator(0, 8)
    assert next(generator) == "0000 0000 0000 0000"
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"


def test_card_number_generator_with_upper_limit():
    generator = card_number_generator(9999999999999996, 10000000000000000)
    assert next(generator) == "9999 9999 9999 9996"
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_empty_transaction_descriptions():
    with pytest.raises(StopIteration):
        generator = transaction_descriptions(list())
        assert next(generator) == "Отсутствуют данные для транзакции"


def test_filter_by_currency():
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
