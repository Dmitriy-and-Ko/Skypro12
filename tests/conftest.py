import pytest


@pytest.fixture()
def standart_numbers_for_get_masks_card_numbers():
    return "3355 89** **** 0921"


@pytest.fixture()
def not_standart_numbers_for_get_masks_card_numbers():
    return "Неправильно задан номер карты. Проверьте номер карты должен содержать 16 цифр"


@pytest.fixture()
def if_card_number_with_letters():
    return "Номер карты должен содержать только цифры"


@pytest.fixture()
def standart_number_for_get_masks_account():
    return "**1849"


@pytest.fixture()
def not_standart_number_for_get_masks_account():
    return "Неправильно задан номер счёта. Проверьте номер счёта должен содержать 20 цифр"


@pytest.fixture()
def if_account_number_contain_letters():
    return "Номер счёта должен содержать только цифры"
