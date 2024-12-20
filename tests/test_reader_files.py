import csv
from pathlib import Path
from dotenv import load_dotenv
import os
from unittest.mock import patch
from src.reader_files import csv_reader, excel_reader, PATH_TO_FILE_CSV, PATH_TO_DIR, PATH_TO_FILE_EXCEL
import pandas as pd


@patch("csv.DictReader")
def test_csv_reader_with_correct_path(mock_dictreader):
    mock_dictreader.return_value = [{"id": 44}]
    assert csv_reader(PATH_TO_FILE_CSV) == [{"id": 44}]


@patch("csv.DictReader")
def test_csv_reader_error(mock_dictreader):
    mock_dictreader.return_value = f"Неверно указан путь к файлу CSV transactions"
    assert csv_reader(PATH_TO_DIR) == f"Неверно указан путь к файлу CSV transactions"


@patch("pandas.read_excel")
def test_excel_reader_with_correct_path(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([{"id": 12}])
    assert excel_reader(PATH_TO_FILE_EXCEL) == [{"id": 12}]


@patch("pandas.read_excel")
def test_excel_reader_error(mock_read_excel):
    mock_read_excel.return_value = f"Неверно указан путь к файлу Excel transactions"
    assert excel_reader(PATH_TO_DIR) == f"Неверно указан путь к файлу Excel transactions"
