import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_or_account, expected", [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                       ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(card_or_account, expected):
    assert mask_account_card(card_or_account) == expected


@pytest.mark.parametrize("card_or_account, expected",[('Счет 73654108430135874305', 'Счет **4305'),
                                                      ('Счет 64686473678000894779589', 'Счет **9589'),
                                                      ('Счет 6468647', 'Счет **8647'),
                                                      ('', 'Ошибка ввода или пустой номер'),
                                                      ('Счет', 'Ошибка ввода или пустой номер'),
                                                      ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                                      ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                      (1596837868705199, '1596 83** **** 5199'),
                                                      (73654108430135874305, '**4305'),
                                                      ('159683786.8705199', 'Ошибка ввода или пустой номер')])
def test_mask_account_card_other_data(card_or_account, expected):
    assert mask_account_card(card_or_account) == expected
