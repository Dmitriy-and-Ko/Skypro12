from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_bank: str) -> str:
    """Фцнкция принимает и маскирует полностью как карту банка, так и номер счёта"""

    list_card = ["visa", "maestro", "master card", "visa classic", "visa platinum", "visa gold"]
    list_bild = ["счёт", "счет"]
    list_data_bank = data_bank.split()
    list_alpha_part_data_bank = list(filter(lambda x: x.isalpha(), list_data_bank))
    list_digit_part_data_bank = list(filter(lambda x: x.isdigit(), list_data_bank))
    string_alpha_part_data_bank = " ".join(list_alpha_part_data_bank)
    string_digit_part_data_bank = "".join(list_digit_part_data_bank)

    if (string_alpha_part_data_bank.lower() in list_card) and (len(string_digit_part_data_bank) == 16):
        return f"{string_alpha_part_data_bank} {get_mask_card_number(string_digit_part_data_bank)}"
    elif (string_alpha_part_data_bank.lower() in list_bild) and len(string_digit_part_data_bank) == 20:
        return f"{string_alpha_part_data_bank} {get_mask_account(string_digit_part_data_bank)}"
    elif len(string_alpha_part_data_bank) == 0 and len(string_digit_part_data_bank) == 16:
        return "Вы не ввели тип карты. Укажите тип карты"
    elif len(string_alpha_part_data_bank) == 0 and len(string_digit_part_data_bank) == 20:
        return "Вы неправильно ввели счёт. Убедитесь, что при вводе перед номером указано слово Счёт"
    else:
        return "Вы ввели некорректный тип карты / счёта, или карта / счёт содержит неверное количество цифр"


def get_date(real_time: str) -> str:
    """Функция принимает время в формате '2024-03-11T02:26:18.671407' и возвращает строку с датой"""
    """в формате 'ДД.ММ.ГГГГ'"""
    if len(real_time) > 10:
        only_date = real_time[:10]
        list_only_date = only_date.split("-")
        sorted_string_only_date = ".".join(reversed(list_only_date))
        return sorted_string_only_date
    return "Неправильно задан формат даты, убедитесь, что дата задана в формате %Y-%m-%dT%H:%M:%S.%f"
