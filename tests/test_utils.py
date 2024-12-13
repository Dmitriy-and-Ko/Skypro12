import os
from unittest.mock import patch

import requests
from unittest import mock

from src.utils import get_list_transactions


@patch('json.load')
def test_get_list_transaction(mock_get):
    mock_get.return_value.json.return_value = []
    assert get_list_transactions('C:\\Users\\user\\OneDrive\\Desktop\\my-prj\\Homework\\data\\operations.json') == []


