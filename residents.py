"""
Модуль для работы с жителями.
"""

from typing import Dict, List, Optional

from utils import generate_id


def add_resident(
    residents: List[Dict[str, any]],
    full_name: str,
    apartment_number: int,
    phone: str,
    status: str
) -> Dict[str, any]:
    """
    Добавить нового жителя.

    Args:
        residents: Список всех жителей
        full_name: ФИО жителя
        apartment_number: Номер квартиры
        phone: Контактный телефон
        status: Статус проживания (Собственник/Арендатор)

    Returns:
        Словарь с данными добавленного жителя
    """
    resident = {
        "id": generate_id(),
        "full_name": full_name,
        "apartment_number": apartment_number,
        "phone": phone,
        "status": status
    }
    residents.append(resident)
    return resident


def find_resident_by_name(
    residents: List[Dict[str, any]],
    query: str
) -> List[Dict[str, any]]:
    """
    Найти жителей по подстроке в ФИО.

    Args:
        residents: Список всех жителей
        query: Поисковый запрос

    Returns:
        Список найденных жителей
    """
    query_lower = query.lower()
    return [
        r for r in residents
        if query_lower in r["full_name"].lower()
    ]


def find_resident_by_apartment(
    residents: List[Dict[str, any]],
    apartment_number: int
) -> Optional[Dict[str, any]]:
    """
    Найти жителя по номеру квартиры.

    Args:
        residents: Список всех жителей
        apartment_number: Номер квартиры

    Returns:
        Словарь с данными жителя или None
    """
    for resident in residents:
        if resident["apartment_number"] == apartment_number:
            return resident
    return None


def get_resident_status(resident: Dict[str, any]) -> str:
    """
    Получить текстовый статус жителя.

    Args:
        resident: Словарь с данными жителя

    Returns:
        Строка со статусом
    """
    return f"{resident['full_name']} - {resident['status']}"


def sort_residents_by_name(
    residents: List[Dict[str, any]]
) -> List[Dict[str, any]]:
    """
    Отсортировать жителей по ФИО.

    Args:
        residents: Список всех жителей

    Returns:
        Отсортированный список жителей
    """
    return sorted(residents, key=lambda r: r["full_name"])
