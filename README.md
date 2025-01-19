# Домашняя работа

Домашняя работа в которой я постепенно создаю банковское приложение,
которое пока способно скрывать номер счета и карты, принимать и выводить
дату в формате ДД.ММ.ГГГГ, сортировать операции по заданным
значениям и по дате. В папке "tests" есть модули тестирования всех функций.

## Установка
Клонируйте репозиторий
  ```bash
   git clone https://github.com/Ingvard12/Home_work.git
   ```

## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
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
