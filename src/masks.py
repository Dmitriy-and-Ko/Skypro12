from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты в формате XXXX XX** **** XXXX, где X - цифра"""
    if len(card_number) != 16:
        return "Неправильно задан номер карты. Проверьте номер карты должен содержать 16 цифр"
    elif card_number.isdigit() is False:
        return "Номер карты должен содержать только цифры"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер счёта в формате **ХХХХ, где XXXX, последние 4 цифры номера"""
    if len(account_number) != 20:
        return "Неправильно задан номер счёта. Проверьте номер счёта должен содержать 20 цифр"
    elif account_number.isdigit() is False:
        return "Номер счёта должен содержать только цифры"
    mask_account_number = f"**{account_number[-4:]}"
    return mask_account_number
