"""
Тесты для класса Resident.
"""

from models.residents import (
    Resident, add_resident, find_resident_by_name, find_resident_by_apartment
)


def test_resident_creation():
    """Тест создания жителя."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    assert resident.id == 1
    assert resident.full_name == "Иванов Иван"
    assert resident.apartment_number == 10
    assert resident.phone == "+7-999-123-4567"
    assert resident.status == "Собственник"


def test_resident_is_owner():
    """Тест проверки статуса собственника."""
    owner = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    tenant = Resident(2, "Петров Пётр", 20, "+7-999-765-4321", "Арендатор")
    assert owner.is_owner()
    assert not tenant.is_owner()


def test_resident_str():
    """Тест строкового представления."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    assert "Иванов Иван" in str(resident)
    assert "Собственник" in str(resident)


def test_add_resident():
    """Тест добавления жителя."""
    residents = []
    resident = add_resident(residents, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    assert len(residents) == 1
    assert resident.full_name == "Иванов Иван"


def test_find_resident_by_name():
    """Тест поиска по ФИО."""
    residents = []
    add_resident(residents, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    add_resident(residents, "Петров Пётр", 20, "+7-999-765-4321", "Арендатор")

    found = find_resident_by_name(residents, "Иванов")
    assert len(found) == 1
    assert found[0].full_name == "Иванов Иван"


def test_find_resident_by_apartment():
    """Тест поиска по квартире."""
    residents = []
    add_resident(residents, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")

    found = find_resident_by_apartment(residents, 10)
    assert found is not None
    assert found.full_name == "Иванов Иван"

    not_found = find_resident_by_apartment(residents, 99)
    assert not_found is None
