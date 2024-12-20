import csv
from pathlib import Path
import pandas as pd
from numpy.ma.core import shape

PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE_CSV = Path(PATH_TO_DIR, 'transactions_files', 'transactions.csv')
PATH_TO_FILE_EXCEL = Path(PATH_TO_DIR, 'transactions_files', 'transactions_excel.xlsx')

def csv_reader(csv_path: str) -> list:
    """Функция считывает финансовые операции из CSV файла принимает путь к файлу CSV в качестве аргумента.
    Результат выводит в виде списка словарей"""
    try:
        if csv_path == PATH_TO_FILE_CSV:
            with open(PATH_TO_FILE_CSV, encoding='utf-8') as file:
                reader = csv.DictReader(file)
                result = list(reader)
                return result
        return f"Неверно указан путь к файлу CSV transactions"
    except Exception as ex:
        return f"Ошибка {ex}"


def excel_reader(excel_path: str) -> list:
    """Функция считывает финансовые операции из excel файла принимает путь к файлу CSV в качестве аргумента.
        Результат выводит в виде списка словарей"""
    try:
        if excel_path == PATH_TO_FILE_EXCEL:
            excel_data = pd.read_excel(PATH_TO_FILE_EXCEL, sheet_name='Лист 1')
            shape_data = excel_data.shape
            list_of_dicts = [dict(excel_data.iloc[x]) for x in range(shape_data[0])]
            return list_of_dicts
        else:
            return f"Неверно указан путь к файлу Excel transactions"
    except Exception as ex:
        return f"Ошибка {ex}"



if __name__ == "__main__":
    print(csv_reader(PATH_TO_FILE_EXCEL))
    print(excel_reader(PATH_TO_FILE_CSV))

    print(excel_reader(PATH_TO_FILE_EXCEL))
    print(excel_reader(PATH_TO_FILE_CSV))
