# Домашнее задание школы программирования Skypro, специализация "Python разработчик"

## Описание
В папке src созданны модули содержащие следующие функции:

+ Модуль masks содержит функции get_mask_card_number и get_mask_account, функция get_mask_card_number Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX , где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. Функция get_mask_account принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки. 

+ Модуль widget содержит функции mask_account_card и get_date. Функция mask_account_card умеет обрабатывать информацию как о картах, так и о счетах. Функция Принимает один аргумент — строку, содержащую тип и номер карты или счета. Функция get_date принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"

+ Модуль processing содержит функции filter_by_state и sort_by_date. функция filter_by_state, принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению. Функция sort_by_date, принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате (date).