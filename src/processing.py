from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по значению ключа 'state'.
    """
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.
    """

    def _parse_to_datetime(transaction: Dict[str, Any]) -> datetime:
        date_str = transaction.get("date")

        if not date_str:
            return datetime.min

        try:
            # Правильный синтаксис для Python 3
            return datetime.fromisoformat(str(date_str))
        except ValueError, TypeError:
            return datetime.min

    return sorted(transactions, key=_parse_to_datetime, reverse=reverse)
