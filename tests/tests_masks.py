from src.masks import get_mask_card_number, get_mask_account

def test_mask_card_number():
    assert get_mask_card_number('3355897567890921') == '3355 89** **** 0921'

def test_mask_card_number_with_wrong_quantity_numbers():
    assert get_mask_card_number('998700560967876543') == 'Неправильно задан номер карты. Проверьте номер карты должен содержать 16 цифр'
    assert get_mask_card_number('12567834902309') == 'Неправильно задан номер карты. Проверьте номер карты должен содержать 16 цифр'


