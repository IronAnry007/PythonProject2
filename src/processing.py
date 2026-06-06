from datetime import datetime


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список транзакций по значению ключа 'state' и
    возвращает новый список словарей, где ключ 'state' равен указанному значению.
    """

    return [new_dict for new_dict in transactions if new_dict.get("state") == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список транзакций по дате.
    """

    def _parse_to_datetime(transaction: dict) -> datetime:
        date_str = transaction.get("date")

        # Если даты нет, возвращаем минимально возможную дату,
        if not date_str:
            return datetime.min

        try:
            return datetime.fromisoformat(str(date_str))
        except ValueError, TypeError:
            return datetime.min

    return sorted(transactions, key=_parse_to_datetime, reverse=reverse)
