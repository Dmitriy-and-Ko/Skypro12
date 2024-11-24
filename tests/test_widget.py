import pytest
from src.widget import mask_account_card

@pytest.mark.parametrize('value, expected', [
    ('Maestro 8820478370895540', 'Maestro 8820 47** **** 5540'),
    ('Master Card 9078458923119865', 'Master Card 9078 45** **** 9865'),
    ('Счет 58093481043826407834', 'Счет **7834'),
    ('4567823456831284', 'Вы не ввели тип карты. Укажите тип карты'),
    ('47092674961430528400', 'Вы неправильно ввели счёт. Убедитесь, что при вводе перед номером указано слово Счёт'),
    ('Visa 1264083456', 'Вы ввели некорректный тип карты / счёта, или карта / счёт содержит неверное количество цифр'),
    ('Счёт 2367901986308764', 'Вы ввели некорректный тип карты / счёта, или карта / счёт содержит неверное количество цифр'),
    ('Visa Gold 23ty34ui56ug4567', 'Вы ввели некорректный тип карты / счёта, или карта / счёт содержит неверное количество цифр'),
    ('visa platinum', 'Вы ввели некорректный тип карты / счёта, или карта / счёт содержит неверное количество цифр'),
    ('Счёт', 'Вы ввели некорректный тип карты / счёта, или карта / счёт содержит неверное количество цифр')
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected