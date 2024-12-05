import pytest
from src.decorators import log



def test_log():
    @log()
    def sum_two_numbers(a, b):
        return a + b
    result = sum_two_numbers(24, 23)
    assert result == 47


