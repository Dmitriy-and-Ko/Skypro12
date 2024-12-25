from numpy.ma.core import choose
from openpyxl.styles.builtins import currency

from src.generators import filter_by_currency
from src.handler_list_tansactions import get_list_with_request_string
from src.processing import filter_by_state, sort_by_date
from src.utils import PATH_TO_FILE_JSON, get_list_transactions
from src.reader_files import PATH_TO_FILE_CSV, PATH_TO_FILE_EXCEL, csv_reader, excel_reader
from src.widget import get_date, mask_account_card

print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:'
    1. Получить информацию о транзакциях из JSON - файла
    2. Получить информацию о транзакциях из CSV - файла
    3. Получить информацию о транзакциях из XLSX - файла''')

if __name__ == '__main__':
    while True:
        # print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:'
        # 1. Получить информацию о транзакциях из JSON - файла
        # 2. Получить информацию о транзакциях из CSV - файла
        # 3. Получить информацию о транзакциях из XLSX - файла''')
        # main_path = str(None)
        choose_file = input('Введите необходимый пункт меню ')
        if choose_file == '1':
            main_path = PATH_TO_FILE_JSON
            main_transactions = get_list_transactions(main_path)
            print('Для обработки выбран JSON-файл')
            break
        elif choose_file == '2':
            main_path = PATH_TO_FILE_CSV
            main_transactions = csv_reader(main_path)
            print('Для обработки выбран CSV-файл')
            break
        elif choose_file == '3':
            main_path = PATH_TO_FILE_EXCEL
            main_transactions = excel_reader(main_path)
            print('Для обработки выбран Excel-файл')
            break
        else:
            print('Введите целое число от 1 до 3')
    # print(main_transactions)
    print('Введите статус, по которому необходимо выполнить фильтрацию.')
    print('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ')
    while True:
        choose_status = input().upper()
        if choose_status == 'EXECUTED' or choose_status == 'CANCELED' or choose_status == 'PENDING':
            by_status_transaction = filter_by_state(main_transactions, choose_status)
            print(f"Операции отфильтрованы по статусу {choose_status}")
            break
        else:
            print(f"Статус операции {choose_status} недоступен.")

    while True:
        data_sort = input('Отсортировать операции по дате? Да/Нет ')
        if data_sort.lower() == 'да':
            while True:
                data_flag = input('Отсортировать по возрастанию или по убыванию? ')
                if data_flag.lower() == 'по возрастанию':
                   by_data_transactions = sort_by_date(by_status_transaction, sort_sequence=False)
                   break
                elif data_flag.lower() == 'по убыванию':
                    by_data_transactions = sort_by_date(by_status_transaction, sort_sequence=True)
                    break
                else:
                    print('Введите значение "по возрастанию" или "по убыванию"')
            break
        elif data_sort.lower() == 'нет':
            by_data_transactions = by_status_transaction
            break
        else:
            print('Введите значение "да" или "нет"')
    while True:
        choose_currency = input('Выводить только рублевые тразакции? Да/Нет ')
        if choose_currency.lower() == 'да':
            transactions_by_rub = list()
            gen_transaction_by_rub = filter_by_currency(by_data_transactions, 'RUB')
            for item in gen_transaction_by_rub:
                transactions_by_rub.append(item)
            break
        elif choose_currency.lower() == 'нет':
            transactions_by_rub = by_data_transactions
            break
        else:
            print('Введите значение "да" или "нет"')
    word_input = input('Отфильтровать список транзакций по определенному слову в описании? ')
    if word_input.lower() == 'да':
        code_word = input('Введите дополнительное описание, для фильтрации (Например: перевод):. ')
        filtered_by_description = get_list_with_request_string(transactions_by_rub, code_word)
    else:
        filtered_by_description = transactions_by_rub

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке:{len(filtered_by_description)}")

    for transaction in filtered_by_description:
        amount = transaction.get('operationAmount', {}).get("amount", {})
        currency_name = transaction.get("operationAmount", {}).get("currency", {}).get("name")
        print(f"{get_date(transaction.get("date"))} {transaction.get("description")}")
        if 'from' not in transaction or 'from' in ['', "", ' ', " "]:
            print(f"{mask_account_card(transaction.get("to"))}")
        else:
            print(f"{mask_account_card(transaction).get('from')} -> {mask_account_card(transaction).get('to')}")
        print(f"Сумма: {amount} {currency_name}")