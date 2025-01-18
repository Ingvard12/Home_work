import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_or_account: str, expected: str) -> None:
    assert mask_account_card(card_or_account) == expected


@pytest.mark.parametrize(
    "card_or_account, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678000894779589", "Счет **9589"),
        ("Счет 6468647", "Счет **8647"),
        ("", "Ошибка ввода или пустой номер"),
        ("Счет", "Ошибка ввода или пустой номер"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        (1596837868705199, "1596 83** **** 5199"),
        (73654108430135874305, "**4305"),
        ("159683786.8705199", "Ошибка ввода или пустой номер"),
    ],
)
def test_mask_account_card_other_data(card_or_account: str, expected: str) -> None:
    assert mask_account_card(card_or_account) == expected


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2019-07-03", "03.07.2019"),
        ("02:26:18.671407T2024-03-11", "11.03.2024"),
        ("", "Отсутствует дата или некорректная запись даты"),
        ("20240311T02:26:18.671407", "Отсутствует дата или некорректная запись даты"),
    ],
)
def test_get_date_other_format(date: str, expected: str) -> None:
    assert get_date(date) == expected
