from src.masks import get_mask_card_number, get_mask_account

def test_mask_card_number(standart_numbers_for_get_masks_card_numbers):
    assert get_mask_card_number('3355897567890921') == standart_numbers_for_get_masks_card_numbers

def test_mask_card_number_with_wrong_quantity_numbers(not_standart_numbers_for_get_masks_card_numbers):
     assert get_mask_card_number('998700560967876543') == not_standart_numbers_for_get_masks_card_numbers
     assert get_mask_card_number('12567834902309') == not_standart_numbers_for_get_masks_card_numbers
     assert get_mask_card_number('456e879h865r786t45') == not_standart_numbers_for_get_masks_card_numbers

def test_empty_mask_card_number(not_standart_numbers_for_get_masks_card_numbers):
     assert get_mask_card_number('') == not_standart_numbers_for_get_masks_card_numbers

def test_letter_in_card_number(if_card_number_with_letters):
     assert get_mask_card_number('456e879h865r786t') == if_card_number_with_letters


def test_mask_account(standart_number_for_get_masks_account):
    assert get_mask_account('36896521479174271849') == standart_number_for_get_masks_account

def test_mask_account_with_wrong_quantity_numbers(not_standart_number_for_get_masks_account):
    assert get_mask_account('2674983417361345') == not_standart_number_for_get_masks_account
    assert get_mask_account('78539725092318368438293') == not_standart_number_for_get_masks_account
    assert get_mask_account('io9034tu67bv8943') == not_standart_number_for_get_masks_account

def test_letter_in_account_number(if_account_number_contain_letters):
    assert get_mask_account('wr897rt748yr287ub905') == if_account_number_contain_letters
