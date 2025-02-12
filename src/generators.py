# import random
from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = "RUB") -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по указанной валюте и возвращает их в виде итератора."""
    found = False
    for t in transactions:
        if t["operationAmount"]["currency"]["code"] == currency:
            found = True
            yield t
    if not found:
        yield "Совпадений не найдено"



def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Возвращает итератор по описаниям транзакций."""
    for tr in transactions:
        yield tr["description"]


def card_number_generator(start: int = 1, stop: int = 4) -> Iterator[str]:
    """Генерирует номера карт в формате "XXXX XXXX XXXX XXXX" в заданном диапазоне"""
    gen_card_numbers = set()
    # while True:
    #     card_gen = str(random.randint(start, stop)) # Заготовка для случайного генератора
    gen_iter = start
    for _ in range(start, stop + 1):
        card_gen = str(gen_iter)
        gen_iter += 1
        while len(card_gen) < 16:
            card_gen = "0" + card_gen
        card_number = f"{card_gen[:4]} {card_gen[4:8]} {card_gen[8:12]} {card_gen[12:16]}"

        if card_number not in gen_card_numbers:
            gen_card_numbers.add(card_number)
            yield card_number


# if __name__ == "__main__":
#
#     transactions = [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160",
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229",
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657",
#         },
#     ]
#
#     usd_transactions = filter_by_currency(transactions, "RUB")
#
#     while True:
#         try:
#             print(next(usd_transactions))
#         except StopIteration:
#             break
#
#     descriptions = transaction_descriptions(transactions)
#     for _ in range(5):
#         try:
#             print(next(descriptions))
#
#         except StopIteration:
#             break
#
#     gen = card_number_generator()
#     for _ in range(10):
#         try:
#             print(next(gen))
#
#         except StopIteration:
#             break
