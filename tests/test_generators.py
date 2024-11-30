import pytest
from src.generators import card_number_generator


def test_card_number_generator():
    generator = card_number_generator(34562812, 34562816)
    assert next(generator) == '0000 0000 3456 2812'
    assert next(generator) == '0000 0000 3456 2813'
    assert next(generator) == '0000 0000 3456 2814'
    assert next(generator) == '0000 0000 3456 2815'


def test_card_number_generator_with_low_limit():
    generator = card_number_generator(0, 8)
    assert next(generator) == '0000 0000 0000 0000'
    assert next(generator) == '0000 0000 0000 0001'
    assert next(generator) == '0000 0000 0000 0002'
    assert next(generator) == '0000 0000 0000 0003'
    assert next(generator) == '0000 0000 0000 0004'


def test_card_number_generator_with_upper_limit():
    generator = card_number_generator(9999999999999996, 10000000000000000)
    assert next(generator) == '9999 9999 9999 9996'
    assert next(generator) == '9999 9999 9999 9997'
    assert next(generator) == '9999 9999 9999 9998'
    assert next(generator) == '9999 9999 9999 9999'
