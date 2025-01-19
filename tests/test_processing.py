from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def key_value() -> str:
    return "EXECUTED"


@pytest.mark.parametrize(
    "list_dict, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [],
        ),
    ],
)
def test_filter_by_state(list_dict: List[Dict[str, Any]], key_value: str, expected: List[Dict[str, Any]]) -> None:
    assert filter_by_state(list_dict, key_value) == expected


@pytest.mark.parametrize(
    "list_dict, sort_by, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(list_dict: List[Dict[str, Any]], sort_by: bool, expected: List[Dict[str, Any]]) -> None:
    assert sort_by_date(list_dict, sort_by) == expected


@pytest.mark.parametrize(
    "list_dict, sort_by, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
            ],
            True,
            [
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
            ],
        ),
    ],
)
def test_sort_by_date_identical(
    list_dict: List[Dict[str, Any]], sort_by: bool, expected: List[Dict[str, Any]]
) -> None:
    assert sort_by_date(list_dict, sort_by) == expected


@pytest.mark.parametrize(
    "list_dict, sort_by, expected",
    [
        ([{"id": 41428829, "state": "EXECUTED", "date": "31-02-2023T18:35:29.512364"}], True, "Не верный формат даты"),
        ([{"id": 594226727, "state": "CANCELED", "date": "2024-02:27:25.241689"}], True, "Не верный формат даты"),
        ([{"id": 615064591, "state": "CANCELED", "date": "31.02.2023:21:33.419441"}], True, "Не верный формат даты"),
    ],
)
def test_sort_by_date_incorrect(list_dict: List[Dict[str, Any]], sort_by: bool, expected: str) -> None:
    assert sort_by_date(list_dict, sort_by) == expected
