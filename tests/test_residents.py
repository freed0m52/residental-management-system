"""
Тесты для модуля residents.py.
"""

from residents import add_resident, find_resident_by_name, find_resident_by_apartment


def test_add_resident():
    """Тест добавления жителя."""
    residents = []
    resident = add_resident(residents, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    assert len(residents) == 1
    assert resident["full_name"] == "Иванов Иван"
    assert resident["apartment_number"] == 10


def test_find_resident_by_name():
    """Тест поиска жителя по ФИО."""
    residents = []
    add_resident(residents, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    add_resident(residents, "Петров Пётр", 20, "+7-999-765-4321", "Арендатор")

    found = find_resident_by_name(residents, "Иванов")
    assert len(found) == 1
    assert found[0]["full_name"] == "Иванов Иван"


def test_find_resident_by_apartment():
    """Тест поиска жителя по номеру квартиры."""
    residents = []
    add_resident(residents, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")

    found = find_resident_by_apartment(residents, 10)
    assert found is not None
    assert found["full_name"] == "Иванов Иван"

    not_found = find_resident_by_apartment(residents, 99)
    assert not_found is None
