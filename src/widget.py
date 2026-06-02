from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """Функция которая принимает строку и возвращает ее с замаскированным номером. """

    if not input_data:
        return "Ошибка: пустая строка"

    new_data = input_data.rsplit(" ", 1)
    card = new_data[0]
    number = new_data[1]

    if len(new_data) != 2:
        return "Ошибка: больше двух подстрок"

    if "Счет" in card:
        encrypted_number = get_mask_account(number)
    else:
        encrypted_number = get_mask_card_number(number)
    return f"{card} {number}"


def get_date(date_string: str) -> str:
    """Преобразует строку с датой из формата '2024-03-11T02:26:18.671407'
    в формат 'ДД.ММ.ГГГГ'."""

    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]
    return f"{day}.{month}.{year}"