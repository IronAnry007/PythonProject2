from datetime import datetime
from typing import TypedDict


class Transaction(TypedDict, total=False):
    id: int
    state: str
    date: str


def filter_by_state(transactions: list[Transaction], state: str = "EXECUTED") -> list[Transaction]:
    """
    Фильтрует список транзакций по значению ключа 'state' и
    возвращает новый список словарей, где ключ 'state' равен указанному значению.
    """

    return [new_dict for new_dict in transactions if new_dict.get("state") == state]


def sort_by_date(transactions: list[Transaction], reverse: bool = True) -> list[Transaction]:
    """
    Сортирует список транзакций по дате.
    """

    def _parse_to_datetime(transaction: Transaction) -> datetime:
        date_str = transaction.get("date")

        # Если даты нет, возвращаем минимально возможную дату,
        if not date_str:
            return datetime.min

        try:
            return datetime.fromisoformat(str(date_str))
        except ValueError, TypeError:
            return datetime.min

    return sorted(transactions, key=_parse_to_datetime, reverse=reverse)
