import os
import json
from json import JSONDecodeError, dumps
from pathlib import Path
import logging
from src.decorators import PATH_TO_FILE
from src.external_api import get_transaction_amount

PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE_JSON = Path(PATH_TO_DIR, "data", "operations.json")
PATH_TO_FILE_LOG = Path(PATH_TO_DIR, "logs", "utils.log")

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(PATH_TO_FILE_LOG, encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_list_transactions(file_path: str) -> list:
    """Функция возвращает список словарей с данными о финансовых транзакциях, на вход принимает путь к файлу"""
    logger.info(f"Проверяем, путь к файлу {PATH_TO_FILE_JSON}")
    if file_path == PATH_TO_FILE_JSON:
        logger.info(f"Путь к файлу {PATH_TO_FILE_JSON} указан верно")
        try:
            with open(PATH_TO_FILE_JSON, "r", encoding="utf-8") as json_file:
                transaction_list = json.load(json_file)
                return transaction_list
        except Exception as ex:
            logger.error(f"Произошла ошибка {ex}")
            return []
    logger.info(f"Путь к файлу {PATH_TO_FILE_JSON} указан не верно")
    return []


if __name__ == "__main__":
    print(get_list_transactions(PATH_TO_FILE))
    print(get_list_transactions(PATH_TO_FILE_JSON))
