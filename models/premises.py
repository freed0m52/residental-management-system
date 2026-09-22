"""
Модуль для работы с помещениями.
"""

from typing import Any, Dict, List, Optional


class Premise:
    """
    Помещение в жилом комплексе.

    Атрибуты:
        id: уникальный идентификатор
        number: номер помещения (квартиры)
        premise_type: тип (жилое/коммерческое)
        area: площадь в кв.м.
        is_occupied: занято ли помещение
    """

    def __init__(
        self,
        premise_id: int,
        number: int,
        premise_type: str,
        area: float,
        is_occupied: bool = False
    ) -> None:
        """Создать объект помещения."""
        self.id = premise_id
        self.number = number
        self.premise_type = premise_type
        self.area = area
        self.is_occupied = is_occupied

    def occupy(self) -> None:
        """Отметить помещение как занятое."""
        self.is_occupied = True

    def vacate(self) -> None:
        """Отметить помещение как свободное."""
        self.is_occupied = False

    def is_living(self) -> bool:
        """Является ли помещение жилым."""
        return self.premise_type == "Жилое"

    def __str__(self) -> str:
        """Строковое представление помещения."""
        status = "занято" if self.is_occupied else "свободно"
        return (
            f"Помещение №{self.number} ({self.premise_type}), "
            f"{self.area} кв.м., {status}"
        )

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "Premise":
        """Создать помещение из словаря (для загрузки из JSON)."""
        return cls(
            premise_id=data["id"],
            number=data["number"],
            premise_type=data["premise_type"],
            area=data["area"],
            is_occupied=data.get("is_occupied", False)
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразовать в словарь (для сохранения в JSON)."""
        return {
            "id": self.id,
            "number": self.number,
            "premise_type": self.premise_type,
            "area": self.area,
            "is_occupied": self.is_occupied
        }


def add_premise(
    premises: List[Premise],
    number: int,
    premise_type: str,
    area: float
) -> Premise:
    """
    Добавить новое помещение.

    Args:
        premises: Список всех помещений
        number: Номер помещения
        premise_type: Тип (Жилое/Коммерческое)
        area: Площадь

    Returns:
        Созданный объект Premise
    """
    from utils import generate_id

    premise = Premise(
        premise_id=generate_id(),
        number=number,
        premise_type=premise_type,
        area=area
    )
    premises.append(premise)
    return premise


def find_premise_by_number(
    premises: List[Premise],
    number: int
) -> Optional[Premise]:
    """
    Найти помещение по номеру.

    Args:
        premises: Список всех помещений
        number: Номер помещения

    Returns:
        Объект Premise или None
    """
    for premise in premises:
        if premise.number == number:
            return premise
    return None


def find_premise_by_id(
    premises: List[Premise],
    premise_id: int
) -> Optional[Premise]:
    """
    Найти помещение по ID.

    Args:
        premises: Список всех помещений
        premise_id: ID помещения

    Returns:
        Объект Premise или None
    """
    for premise in premises:
        if premise.id == premise_id:
            return premise
    return None


def filter_premises_by_type(
    premises: List[Premise],
    premise_type: str
) -> List[Premise]:
    """
    Отобрать помещения по типу.

    Args:
        premises: Список всех помещений
        premise_type: Тип помещения

    Returns:
        Список помещений нужного типа
    """
    return [p for p in premises if p.premise_type == premise_type]


def sort_premises_by_area(
    premises: List[Premise]
) -> List[Premise]:
    """
    Отсортировать помещения по площади.

    Args:
        premises: Список всех помещений

    Returns:
        Отсортированный список
    """
    return sorted(premises, key=lambda p: p.area)


def show_premises(premises: List[Premise]) -> None:
    """
    Вывести список всех помещений.

    Args:
        premises: Список всех помещений
    """
    if not premises:
        print("\n📋 Список помещений пуст.")
        return

    print("\n" + "=" * 60)
    print("🏠 СПИСОК ПОМЕЩЕНИЙ")
    print("=" * 60)

    for premise in premises:
        print(f"ID: {premise.id}")
        print(f"  {premise}")
        print("-" * 40)
