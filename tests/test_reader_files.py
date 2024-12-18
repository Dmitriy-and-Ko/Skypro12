import csv
from pathlib import Path
from dotenv import load_dotenv
import os
from unittest.mock import patch
from src.reader_files import csv_reader, PATH_TO_FILE_CSV, PATH_TO_DIR


@patch('csv.DictReader')
def test_csv_reader_with_correct_path(mock_dictreader):
  mock_dictreader.return_value = [{"id": 44}]
  assert csv_reader(PATH_TO_FILE_CSV) == [{"id": 44}]

@patch('csv.DictReader')
def test_csv_reader_error(mock_dictreader):
  mock_dictreader.return_value = f"Неверно указан путь к файлу CSV transactions"
  assert csv_reader(PATH_TO_DIR) == f"Неверно указан путь к файлу CSV transactions"