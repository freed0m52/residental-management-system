"""
Модуль для работы с заявками на обслуживание.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from .residents import Resident


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


class Request:
    """
    Заявка на обслуживание.

    Атрибуты:
        id: уникальный идентификатор
        resident: объект Resident (житель, подавший заявку)
        apartment_number: номер квартиры
        request_type: тип заявки
        description: описание проблемы
        is_urgent: срочность
        status: статус (Новая/Срочная/Выполнена)
        created_at: дата и время создания
        department: ответственный отдел
    """

    def __init__(
        self,
        request_id: int,
        resident: Resident,
        apartment_number: int,
        request_type: str,
        description: str,
        is_urgent: bool = False,
        status: str = "",
        created_at: str = "",
        department: str = ""
    ) -> None:
        """Создать объект заявки."""
        self.id = request_id
        self.resident = resident
        self.apartment_number = apartment_number
        self.request_type = request_type
        self.description = description
        self.is_urgent = is_urgent

        # Статус: если передан явно — используем его,
        # иначе определяем по срочности
        if status:
            self.status = status
        else:
            self.status = "Срочная" if is_urgent else "Новая"

        self.created_at = created_at or datetime.now().strftime("%d.%m.%Y %H:%M")
        self.department = department or self._get_department()

    def _get_department(self) -> str:
        """Определить ответственный отдел."""
        if self.is_urgent:
            return "Старший мастер"
        return DEPARTMENTS.get(self.request_type, "Общий отдел")

    def complete(self) -> None:
        """Отметить заявку как выполненную."""
        self.status = "Выполнена"

    def mark_urgent(self) -> None:
        """Сделать заявку срочной."""
        self.is_urgent = True
        self.status = "Срочная"
        self.department = "Старший мастер"

    def is_completed(self) -> bool:
        """Проверить, выполнена ли заявка."""
        return self.status == "Выполнена"

    def __str__(self) -> str:
        """Строковое представление заявки."""
        urgent = "⚠️ СРОЧНО " if self.is_urgent else ""
        return (
            f"{urgent}Заявка №{self.id}: {self.request_type} "
            f"(кв. {self.apartment_number}), статус: {self.status}"
        )

    @classmethod
    def from_data(
        cls,
        data: Dict[str, Any],
        residents: List[Resident]
    ) -> Optional["Request"]:
        """
        Создать заявку из словаря (для загрузки из JSON).

        Args:
            data: Словарь с данными заявки
            residents: Список жителей для восстановления связи
        """
        resident = None
        for r in residents:
            if r.id == data["resident_id"]:
                resident = r
                break

        if resident is None:
            return None

        return cls(
            request_id=data["id"],
            resident=resident,
            apartment_number=data["apartment_number"],
            request_type=data["type"],
            description=data["description"],
            is_urgent=data.get("is_urgent", False),
            status=data.get("status", ""),
            created_at=data.get("created_at", ""),
            department=data.get("department", "")
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразовать в словарь (для сохранения в JSON)."""
        return {
            "id": self.id,
            "resident_id": self.resident.id,
            "apartment_number": self.apartment_number,
            "type": self.request_type,
            "description": self.description,
            "is_urgent": self.is_urgent,
            "status": self.status,
            "created_at": self.created_at,
            "department": self.department
        }


def create_request(
    requests: List[Request],
    resident: Resident,
    apartment_number: int,
    request_type: str,
    description: str,
    is_urgent: bool = False
) -> Request:
    """
    Создать новую заявку.

    Args:
        requests: Список всех заявок
        resident: Объект жителя
        apartment_number: Номер квартиры
        request_type: Тип заявки
        description: Описание
        is_urgent: Срочность

    Returns:
        Созданный объект Request
    """
    from utils import generate_id

    request = Request(
        request_id=generate_id(),
        resident=resident,
        apartment_number=apartment_number,
        request_type=request_type,
        description=description,
        is_urgent=is_urgent
    )
    requests.append(request)
    return request


def find_requests_by_apartment(
    requests: List[Request],
    apartment_number: int
) -> List[Request]:
    """Найти заявки по номеру квартиры."""
    return [r for r in requests if r.apartment_number == apartment_number]


def find_requests_by_status(
    requests: List[Request],
    status: str
) -> List[Request]:
    """Найти заявки по статусу."""
    return [r for r in requests if r.status.lower() == status.lower()]


def find_requests_by_resident(
    requests: List[Request],
    resident: Resident
) -> List[Request]:
    """Найти заявки конкретного жителя."""
    return [r for r in requests if r.resident.id == resident.id]


def update_request_status(
    requests: List[Request],
    request_id: int,
    new_status: str
) -> bool:
    """Обновить статус заявки."""
    for request in requests:
        if request.id == request_id:
            request.status = new_status
            return True
    return False


def get_requests_summary(requests: List[Request]) -> Dict[str, int]:
    """Получить статистику по заявкам."""
    summary = {
        "Всего": len(requests),
        "Новые": 0,
        "Срочные": 0,
        "Выполненные": 0
    }

    for r in requests:
        if r.status == "Новая":
            summary["Новые"] += 1
        elif r.status == "Выполнена":
            summary["Выполненные"] += 1

        if r.is_urgent:
            summary["Срочные"] += 1

    return summary


def show_requests(requests: List[Request]) -> None:
    """Вывести список всех заявок."""
    if not requests:
        print("\n📋 Список заявок пуст.")
        return

    print("\n" + "=" * 60)
    print("📝 СПИСОК ЗАЯВОК")
    print("=" * 60)

    for request in requests:
        print(f"ID: {request.id}")
        print(f"  {request}")
        print(f"  Житель: {request.resident.full_name}")
        print(f"  Описание: {request.description}")
        print(f"  Отдел: {request.department}")
        print(f"  Дата: {request.created_at}")
        print("-" * 40)
