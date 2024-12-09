import pytest
from src.decorators import log


def sum_two_numbers(a, b):
    return a + b


def test_log():
    @log()
    def sum_two_numbers(a, b):
        return a + b

    result = sum_two_numbers(24, 23)
    assert result == 47


def test_log_with_different_type_of_arguments(capsys):
    @log()
    def sum_two_numbers(a, b):
        return a + b
    sum_two_numbers('24', 22)
    captured = capsys.readouterr()
    assert captured.out == "Функция выполнена с ошибкой\n"
