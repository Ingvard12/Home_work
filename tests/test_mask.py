import pytest

from src.mask import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'


@pytest.mark.parametrize("card_number, expected", [(700079228960636, '7000 79** **** 0636'),
                                                   (73654108430135874305, '7365 41** **** 4305'),
                                                   (7000790636, '7000 79** **** 0636')
                                                   ])
def test_get_mask_card_number_other_length(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == "Номер карты не может быть пустым"


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == '**4305'


@pytest.mark.parametrize("account, expected", [(73654108430453626135874315, '**4315'),
                                               (73654325, '**4325'),
                                               ('73654108430135874345', '**4345'),
                                               (355, '**355')
                                               ])
def test_get_mask_account_other_length(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_account_empty():
    assert get_mask_account('') == "Номер счета не может быть пустым"
