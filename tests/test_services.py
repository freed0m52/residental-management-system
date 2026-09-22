"""
Тесты для класса Service.
"""

from models.services import (
    Service, add_service, find_service_by_name, get_active_services
)


def test_service_creation():
    """Тест создания услуги."""
    service = Service(1, "Парковка", 3000.0, "Ежемесячно")
    assert service.id == 1
    assert service.name == "Парковка"
    assert service.cost == 3000.0
    assert service.period == "Ежемесячно"
    assert service.is_active


def test_service_annual_cost():
    """Тест годовой стоимости."""
    monthly = Service(1, "Парковка", 3000.0, "Ежемесячно")
    once = Service(2, "Клининг", 5000.0, "Разово")

    assert monthly.get_annual_cost() == 36000.0
    assert once.get_annual_cost() == 5000.0


def test_service_activate_deactivate():
    """Тест активации и деактивации."""
    service = Service(1, "Парковка", 3000.0, "Ежемесячно")
    service.deactivate()
    assert not service.is_active
    service.activate()
    assert service.is_active


def test_service_str():
    """Тест строкового представления."""
    service = Service(1, "Парковка", 3000.0, "Ежемесячно")
    assert "Парковка" in str(service)
    assert "3000" in str(service)


def test_add_service():
    """Тест добавления услуги."""
    services = []
    add_service(services, "Парковка", 3000.0, "Ежемесячно")
    assert len(services) == 1


def test_find_service_by_name():
    """Тест поиска услуги по названию."""
    services = []
    add_service(services, "Парковка", 3000.0, "Ежемесячно")
    add_service(services, "Клининг", 5000.0, "Разово")

    found = find_service_by_name(services, "Парковка")
    assert len(found) == 1


def test_get_active_services():
    """Тест получения активных услуг."""
    services = []
    add_service(services, "Парковка", 3000.0, "Ежемесячно")
    s2 = add_service(services, "Клининг", 5000.0, "Разово")
    s2.deactivate()

    active = get_active_services(services)
    assert len(active) == 1
    assert active[0].name == "Парковка"
