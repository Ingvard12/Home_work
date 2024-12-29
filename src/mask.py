def get_mask_card_number(card_number: int) -> str:
    """Создает маску из введенного номера карты"""
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account: int) -> str:
    """Создает маску номера счета"""
    return f"**{str(account)[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
