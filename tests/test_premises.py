"""
Тесты для класса Premise.
"""

from models.premises import (
    Premise, add_premise, find_premise_by_number, filter_premises_by_type
)


def test_premise_creation():
    """Тест создания помещения."""
    premise = Premise(1, 45, "Жилое", 60.5)
    assert premise.id == 1
    assert premise.number == 45
    assert premise.premise_type == "Жилое"
    assert premise.area == 60.5
    assert not premise.is_occupied


def test_premise_occupy_vacate():
    """Тест занятия и освобождения."""
    premise = Premise(1, 45, "Жилое", 60.5)
    premise.occupy()
    assert premise.is_occupied
    premise.vacate()
    assert not premise.is_occupied


def test_premise_is_living():
    """Тест проверки типа."""
    living = Premise(1, 45, "Жилое", 60.5)
    commercial = Premise(2, 1, "Коммерческое", 100.0)
    assert living.is_living()
    assert not commercial.is_living()


def test_premise_str():
    """Тест строкового представления."""
    premise = Premise(1, 45, "Жилое", 60.5)
    assert "45" in str(premise)
    assert "Жилое" in str(premise)


def test_add_premise():
    """Тест добавления помещения."""
    premises = []
    add_premise(premises, 10, "Жилое", 50.0)
    assert len(premises) == 1


def test_find_premise_by_number():
    """Тест поиска по номеру."""
    premises = []
    add_premise(premises, 10, "Жилое", 50.0)
    add_premise(premises, 20, "Коммерческое", 100.0)

    found = find_premise_by_number(premises, 10)
    assert found is not None
    assert found.number == 10

    not_found = find_premise_by_number(premises, 99)
    assert not_found is None


def test_filter_premises_by_type():
    """Тест фильтрации по типу."""
    premises = []
    add_premise(premises, 10, "Жилое", 50.0)
    add_premise(premises, 20, "Коммерческое", 100.0)
    add_premise(premises, 30, "Жилое", 70.0)

    living = filter_premises_by_type(premises, "Жилое")
    assert len(living) == 2
