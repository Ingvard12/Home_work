# Домашняя работа

Домашняя работа в которой я постепенно создаю банковское приложение,
которое пока способно скрывать номер счета и карты, принимать и выводить
дату в формате ДД.ММ.ГГГГ, сортировать операции по заданным
значениям и по дате.

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