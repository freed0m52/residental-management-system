"""
Модуль для работы с заявками на обслуживание.
"""

from datetime import datetime
from typing import Dict, List

from utils import generate_id


REQUEST_TYPES = {
    "1": "Ремонт",
    "2": "Уборка",
    "3": "Сантехника"
}

DEPARTMENTS = {
    "Сантехника": "Отдел технического обслуживания",
    "Ремонт": "Отдел технического обслуживания",
    "Уборка": "Общий отдел"
}


def create_request(
    requests: List[Dict[str, any]],
    resident_id: int,
    apartment_number: int,
    request_type: str,
    description: str,
    is_urgent: bool = False
) -> Dict[str, any]:
    """
    Создать новую заявку на обслуживание.

    Args:
        requests: Список всех заявок
        resident_id: ID жителя
        apartment_number: Номер квартиры
        request_type: Тип заявки
        description: Описание проблемы
        is_urgent: Флаг срочности

    Returns:
        Словарь с данными созданной заявки
    """
    current_date = datetime.now()

    request = {
        "id": generate_id(),
        "resident_id": resident_id,
        "apartment_number": apartment_number,
        "type": request_type,
        "description": description,
        "is_urgent": is_urgent,
        "status": "Срочная" if is_urgent else "Новая",
        "created_at": current_date.strftime("%d.%m.%Y %H:%M"),
        "department": get_department(request_type, is_urgent)
    }
    requests.append(request)
    return request


def get_department(request_type: str, is_urgent: bool) -> str:
    """
    Определить ответственный отдел.

    Args:
        request_type: Тип заявки
        is_urgent: Флаг срочности

    Returns:
        Название отдела
    """
    if is_urgent:
        return "Старший мастер"
    return DEPARTMENTS.get(request_type, "Общий отдел")


def find_requests_by_apartment(
    requests: List[Dict[str, any]],
    apartment_number: int
) -> List[Dict[str, any]]:
    """
    Найти все заявки по номеру квартиры.

    Args:
        requests: Список всех заявок
        apartment_number: Номер квартиры

    Returns:
        Список заявок
    """
    return [
        r for r in requests
        if r["apartment_number"] == apartment_number
    ]


def find_requests_by_status(
    requests: List[Dict[str, any]],
    status: str
) -> List[Dict[str, any]]:
    """
    Найти заявки по статусу.

    Args:
        requests: Список всех заявок
        status: Статус заявки

    Returns:
        Список заявок
    """
    return [
        r for r in requests
        if r["status"].lower() == status.lower()
    ]


def update_request_status(
    requests: List[Dict[str, any]],
    request_id: int,
    new_status: str
) -> bool:
    """
    Обновить статус заявки.

    Args:
        requests: Список всех заявок
        request_id: ID заявки
        new_status: Новый статус

    Returns:
        True если обновлено, False если заявка не найдена
    """
    for request in requests:
        if request["id"] == request_id:
            request["status"] = new_status
            return True
    return False


def get_request_status_text(is_available: bool) -> str:
    """
    Вернуть текстовый статус (функция из ПР1).

    Args:
        is_available: Доступность

    Returns:
        Текстовый статус
    """
    if is_available:
        return "Помещение доступно для бронирования"
    return "Помещение уже занято"


def get_requests_summary(requests: List[Dict[str, any]]) -> Dict[str, int]:
    """
    Получить статистику по заявкам.

    Args:
        requests: Список всех заявок

    Returns:
        Словарь со статистикой
    """
    summary = {
        "Всего": len(requests),
        "Новые": 0,
        "Срочные": 0,
        "Выполненные": 0
    }

    for r in requests:
        if r["status"] == "Новая":
            summary["Новые"] += 1
        elif r["status"] == "Выполнена":
            summary["Выполненные"] += 1

        if r.get("is_urgent", False):
            summary["Срочные"] += 1

    return summary
