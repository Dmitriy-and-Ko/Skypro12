import datetime
from typing import Union


def filter_by_state(dictionary_list: Union[list, dict], state: str = "EXECUTED") -> Union[list, dict]:
    """Функция возвращающая из списка словарей список,
    в которых ключ state равен определённому пользавателем значению"""
    sorted_dictionary_list = list()
    for user_dictionary in dictionary_list:
        if user_dictionary.get("state") == state:
            sorted_dictionary_list.append(user_dictionary)
    return sorted_dictionary_list


def sort_by_date(list_of_dictionary: Union[list, dict], sort_sequence: bool = True) -> Union[list, dict]:
    """Функция, сортирующая список словарей по дате"""
    list_with_date = list()
    for my_dictionary in list_of_dictionary:
        if "date" in my_dictionary.keys():
            list_with_date.append(my_dictionary)
    sorted_of_date_list = sorted(
        list_with_date,
        key=lambda x: datetime.datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=sort_sequence,
    )
    return sorted_of_date_list
