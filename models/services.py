"""
Модуль для работы с дополнительными услугами.
"""

from typing import Any, Dict, List, Optional


class Service:
    """
    Дополнительная услуга для жильцов.

    Атрибуты:
        id: уникальный идентификатор
        name: название услуги
        cost: стоимость в рублях
        period: периодичность (Ежемесячно/Разово)
        is_active: активна ли услуга
    """

    def __init__(
        self,
        service_id: int,
        name: str,
        cost: float,
        period: str,
        is_active: bool = True
    ) -> None:
        """Создать объект услуги."""
        self.id = service_id
        self.name = name
        self.cost = cost
        self.period = period
        self.is_active = is_active

    def activate(self) -> None:
        """Активировать услугу."""
        self.is_active = True

    def deactivate(self) -> None:
        """Деактивировать услугу."""
        self.is_active = False

    def get_annual_cost(self) -> float:
        """Рассчитать годовую стоимость услуги."""
        if self.period == "Ежемесячно":
            return self.cost * 12
        return self.cost

    def __str__(self) -> str:
        """Строковое представление услуги."""
        status = "активна" if self.is_active else "неактивна"
        return (
            f"Услуга '{self.name}': {self.cost} руб. "
            f"({self.period}), {status}"
        )

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "Service":
        """Создать услугу из словаря."""
        return cls(
            service_id=data["id"],
            name=data["name"],
            cost=data["cost"],
            period=data["period"],
            is_active=data.get("is_active", True)
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразовать в словарь."""
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "period": self.period,
            "is_active": self.is_active
        }


def add_service(
    services: List[Service],
    name: str,
    cost: float,
    period: str
) -> Service:
    """
    Добавить новую услугу.

    Args:
        services: Список всех услуг
        name: Название услуги
        cost: Стоимость
        period: Периодичность

    Returns:
        Созданный объект Service
    """
    from utils import generate_id

    service = Service(
        service_id=generate_id(),
        name=name,
        cost=cost,
        period=period
    )
    services.append(service)
    return service


def find_service_by_name(
    services: List[Service],
    query: str
) -> List[Service]:
    """
    Найти услуги по подстроке в названии.

    Args:
        services: Список всех услуг
        query: Поисковый запрос

    Returns:
        Список найденных услуг
    """
    query_lower = query.lower()
    return [s for s in services if query_lower in s.name.lower()]


def find_service_by_id(
    services: List[Service],
    service_id: int
) -> Optional[Service]:
    """
    Найти услугу по ID.

    Args:
        services: Список всех услуг
        service_id: ID услуги

    Returns:
        Объект Service или None
    """
    for service in services:
        if service.id == service_id:
            return service
    return None


def get_active_services(services: List[Service]) -> List[Service]:
    """
    Получить список активных услуг.

    Args:
        services: Список всех услуг

    Returns:
        Список активных услуг
    """
    return [s for s in services if s.is_active]


def sort_services_by_cost(
    services: List[Service]
) -> List[Service]:
    """
    Отсортировать услуги по стоимости.

    Args:
        services: Список всех услуг

    Returns:
        Отсортированный список
    """
    return sorted(services, key=lambda s: s.cost)


def show_services(services: List[Service]) -> None:
    """
    Вывести список всех услуг.

    Args:
        services: Список всех услуг
    """
    if not services:
        print("\n📋 Список услуг пуст.")
        return

    print("\n" + "=" * 60)
    print("💼 СПИСОК УСЛУГ")
    print("=" * 60)

    for service in services:
        print(f"ID: {service.id}")
        print(f"  {service}")
        print(f"  Годовая стоимость: {service.get_annual_cost()} руб.")
        print("-" * 40)
