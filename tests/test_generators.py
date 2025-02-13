from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions_list() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency(transactions_list: List[Dict[str, Any]]) -> None:
    filtered_transactions = list(filter_by_currency(transactions_list, "RUB"))
    expected_result = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert filtered_transactions == expected_result


def test_filter_by_currency_no_currency(transactions_list: List[Dict[str, Any]]) -> None:
    filtered_transactions = list(filter_by_currency(transactions_list, "EUR"))
    expected_result = ["Совпадений не найдено"]
    assert filtered_transactions == expected_result


def test_filter_by_currency_empty(transactions_list: List[Dict[str, Any]]) -> None:
    filtered_transactions = list(filter_by_currency([], "RUB"))
    expected_result = ["Совпадений не найдено"]
    assert filtered_transactions == expected_result


def test_transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> None:
    filtered_transactions = list(transaction_descriptions(transactions_list))
    expected_result = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert filtered_transactions == expected_result


def test_transaction_descriptions_empty(transactions_list: List[Dict[str, Any]]) -> None:
    filtered_transactions = list(transaction_descriptions([]))
    assert filtered_transactions == []


def test_card_number_generator() -> None:
    card_gen = list(card_number_generator(1, 5))
    expected_result = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert card_gen == expected_result


def test_card_number_format() -> None:
    card_gen = list(card_number_generator(1, 5))
    for card_num in card_gen:
        assert len(card_num) == 19
        assert len(card_num.split()) == 4


def test_card_number_edge_cases() -> None:
    card_gen = list(card_number_generator(10, 10))
    assert len(card_gen) == 1
    card_gen = list(card_number_generator(10, 5))
    expected_result = [
        "0000 0000 0000 0005",
        "0000 0000 0000 0006",
        "0000 0000 0000 0007",
        "0000 0000 0000 0008",
        "0000 0000 0000 0009",
        "0000 0000 0000 0010",
    ]
    assert card_gen == expected_result
