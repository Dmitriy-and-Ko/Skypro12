from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты в формате XXXX XX** **** XXXX, где X - цифра"""
    if len(card_number) != 16:
        return 'Неправильно задан номер карты. Проверьте номер карты должен содержать 16 цифр'
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер счёта в формате **ХХХХ, где XXXX, последние 4 цифры номера"""

    mask_account_number = f"**{account_number[-5:-1]}"
    return mask_account_number
