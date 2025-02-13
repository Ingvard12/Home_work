# Домашняя работа

Домашняя работа в которой я постепенно создаю банковское приложение.
Приложение пока способно скрывать номер счета и карты, принимать и выводить
дату в формате ДД.ММ.ГГГГ, сортировать операции по заданным
значениям и по дате, фильтрует транзакции по указанной валюте, выводить 
описания транзакций и генерировать номера карт в заданном диапазоне. В папке "tests" есть модули тестирования всех функций.

## Установка
Клонируйте репозиторий
  ```bash
   git clone https://github.com/Ingvard12/Home_work.git
   ```

## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)

transactions = [
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
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]

# Фильтрация транзакций по валюте
rub_transactions = list(filter_by_currency(transactions, "RUB"))
print(rub_transactions)

# Получение описаний всех транзакций
descriptions = list(transaction_descriptions(transactions))
print(descriptions)

# Генерация номеров карт в заданном диапазоне
card_numbers = list(card_number_generator(1, 5))
print(card_numbers)
```
## Тестирование
Примеры использования функций тестирования:
```python
import pytest

from src.mask import get_mask_account, get_mask_card_number

# Пример тестирования  get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [(700079228960636, '7000 79** **** 0636'),
                                                   (73654108430135874305, '7365 41** **** 4305'),
                                                   (7000790636, '7000 79** **** 0636')
                                                   ])
def test_get_mask_card_number_other_length(card_number, expected):
    assert get_mask_card_number(card_number) == expected
    
# Пример тестирования get_mask_account 
@pytest.mark.parametrize("account, expected", [(73654108430453626135874315, '**4315'),
                                               (73654325, '**4325'),
                                               ('73654108430135874345', '**4345'),
                                               (355, '**355')
                                               ])
def test_get_mask_account_other_length(account, expected):
    assert get_mask_account(account) == expected
```
