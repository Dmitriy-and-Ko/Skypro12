from typing import Union
import logging
from pathlib import Path

PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE_LOG = Path(PATH_TO_DIR, 'logs', 'masks.log')

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler =  logging.FileHandler(PATH_TO_FILE_LOG, encoding='UTF-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)



def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты в формате XXXX XX** **** XXXX, где X - цифра"""
    if len(card_number) != 16:
        logger.info(f"Номер карты не содержит 16 цифр.")
        return "Неправильно задан номер карты. Проверьте номер карты должен содержать 16 цифр"
    elif card_number.isdigit() is False:
        logger.info(f"В 16-ти разрядном номере карты обнаружены буквы.")
        return "Номер карты должен содержать только цифры"
    logger.info(f"Маскировка номера карты проведена успешно.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер счёта в формате **ХХХХ, где XXXX, последние 4 цифры номера"""
    if len(account_number) != 20:
        logger.info(f"Номер счёта не содержит 20 цифр.")
        return "Неправильно задан номер счёта. Проверьте номер счёта должен содержать 20 цифр"
    elif account_number.isdigit() is False:
        logger.info(f"В 20-ти разрядном номере счёта обнаружены буквы.")
        return "Номер счёта должен содержать только цифры"
    mask_account_number = f"**{account_number[-4:]}"
    logger.info(f"Маскировка номера счёта проведена успешно.")
    return mask_account_number

if __name__ == '__main__':
    get_mask_card_number('346923')
    get_mask_card_number('1267e859i907k096')
    get_mask_card_number('1267385949077096')
    get_mask_account('0909567898')
    get_mask_account('090x476v332i446u631f')
    get_mask_account('09034768332544646318')

