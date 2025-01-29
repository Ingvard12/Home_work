from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(list_dict: List[Dict[str, Any]], key_value: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей операций и возвращает только те в которых значечение ключа 'state'
    соответствует указанному в функции, по умолчанию 'EXECUTED'"""
    new_list = []
    for operation in list_dict:
        if operation["state"] == key_value:
            new_list.append(operation)
    return new_list


def sort_by_date(list_dict: List[Dict[str, Any]], sort_by: bool = False) -> Any:
    """Сортирует списки словарей операций по дате, по умолчанию от последней даты до первой"""
    for i in list_dict:
        date_format = i["date"]
        try:
            datetime.strptime(date_format, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            date_format = 'Не верный формат даты'
        else:
            date_format = sorted(list_dict, key=lambda x: x["date"], reverse=sort_by)
        finally:
            return date_format


# if __name__ == "__main__":
#     print(
#         filter_by_state(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ]
#         )
#     )
#
#     print(
#         sort_by_date(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ]
#         )
#     )
