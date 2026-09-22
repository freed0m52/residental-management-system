"""
Модуль для работы с жителями.
"""

from typing import Any, Dict, List, Optional


class Resident:
    """
    Житель жилого комплекса.

    Атрибуты:
        id: уникальный идентификатор
        full_name: ФИО жителя
        apartment_number: номер квартиры
        phone: контактный телефон
        status: статус проживания (Собственник/Арендатор)
    """

    def __init__(
        self,
        resident_id: int,
        full_name: str,
        apartment_number: int,
        phone: str,
        status: str
    ) -> None:
        """Создать объект жителя."""
        self.id = resident_id
        self.full_name = full_name
        self.apartment_number = apartment_number
        self.phone = phone
        self.status = status

    def is_owner(self) -> bool:
        """Является ли житель собственником."""
        return self.status == "Собственник"

    def __str__(self) -> str:
        """Строковое представление жителя."""
        return (
            f"{self.full_name} (кв. {self.apartment_number}), "
            f"{self.status}, тел. {self.phone}"
        )

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "Resident":
        """Создать жителя из словаря (для загрузки из JSON)."""
        return cls(
            resident_id=data["id"],
            full_name=data["full_name"],
            apartment_number=data["apartment_number"],
            phone=data["phone"],
            status=data["status"]
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразовать в словарь (для сохранения в JSON)."""
        return {
            "id": self.id,
            "full_name": self.full_name,
            "apartment_number": self.apartment_number,
            "phone": self.phone,
            "status": self.status
        }


def add_resident(
    residents: List[Resident],
    full_name: str,
    apartment_number: int,
    phone: str,
    status: str
) -> Resident:
    """
    Добавить нового жителя.

    Args:
        residents: Список всех жителей
        full_name: ФИО жителя
        apartment_number: Номер квартиры
        phone: Телефон
        status: Статус проживания

    Returns:
        Созданный объект Resident
    """
    from utils import generate_id

    resident = Resident(
        resident_id=generate_id(),
        full_name=full_name,
        apartment_number=apartment_number,
        phone=phone,
        status=status
    )
    residents.append(resident)
    return resident


def find_resident_by_name(
    residents: List[Resident],
    query: str
) -> List[Resident]:
    """
    Найти жителей по подстроке в ФИО.

    Args:
        residents: Список всех жителей
        query: Поисковый запрос

    Returns:
        Список найденных жителей
    """
    query_lower = query.lower()
    return [r for r in residents if query_lower in r.full_name.lower()]


def find_resident_by_apartment(
    residents: List[Resident],
    apartment_number: int
) -> Optional[Resident]:
    """
    Найти жителя по номеру квартиры.

    Args:
        residents: Список всех жителей
        apartment_number: Номер квартиры

    Returns:
        Объект Resident или None
    """
    for resident in residents:
        if resident.apartment_number == apartment_number:
            return resident
    return None


def find_resident_by_id(
    residents: List[Resident],
    resident_id: int
) -> Optional[Resident]:
    """
    Найти жителя по ID.

    Args:
        residents: Список всех жителей
        resident_id: ID жителя

    Returns:
        Объект Resident или None
    """
    for resident in residents:
        if resident.id == resident_id:
            return resident
    return None


def sort_residents_by_name(
    residents: List[Resident]
) -> List[Resident]:
    """
    Отсортировать жителей по ФИО.

    Args:
        residents: Список всех жителей

    Returns:
        Отсортированный список
    """
    return sorted(residents, key=lambda r: r.full_name)


def show_residents(residents: List[Resident]) -> None:
    """
    Вывести список всех жителей.

    Args:
        residents: Список всех жителей
    """
    if not residents:
        print("\n📋 Список жителей пуст.")
        return

    print("\n" + "=" * 60)
    print("👥 СПИСОК ЖИТЕЛЕЙ")
    print("=" * 60)

    for resident in sort_residents_by_name(residents):
        print(f"ID: {resident.id}")
        print(f"  {resident}")
        print("-" * 40)
