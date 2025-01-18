from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Принимает тип и номер карты или счета и создает их маску"""
    account_text = ""
    account_nums = ""

    account_list = str(account_card).split(" ")
    if "Счет" not in account_list:
        for element in account_list:
            if element.isdigit():
                if len(str(element)) == 16:
                    account_nums = str(get_mask_card_number(element))
                else:
                    account_nums = str(get_mask_account(element))
            else:
                account_text += element
                account_text += " "
    else:
        for element in account_list:
            if element.isdigit():
                account_nums = str(get_mask_account(element))
            else:
                account_text += element
                account_text += " "
    if account_nums == "":
        return "Ошибка ввода или пустой номер"
    return account_text + account_nums


def get_date(date: str) -> str:
    """Принимает дату и выводит в формате ДД.ММ.ГГГГ"""
    split_date = date.split("T")
    if "-" in date:
        for element in split_date:
            if "-" in element:
                new_date = element.split("-")
                return f"{new_date[-1]}.{new_date[-2]}.{new_date[-3]}"
    else:
        return "Отсутствует дата или некорректная запись даты"
    return ""


# if __name__ == "__main__":
#     print(mask_account_card("Visa Platinum 7000792289606361"))
#     print(mask_account_card("Maestro 1596837868705199"))
#     print(mask_account_card("Счет 73654108430135874305"))
#     print(mask_account_card("Счет 64686473678894779589"))
#     print(mask_account_card("Visa Classic 6831982476737658"))
#     print(mask_account_card("Visa Gold 5999414228426353"))
#     print(mask_account_card("MasterCard 7158300734726758"))
#
# print(get_date("2024-03-11T02:26:18.671407"))
