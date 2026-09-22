"""
Тесты для класса Request.
"""

from models.residents import Resident
from models.requests import (
    Request, create_request, find_requests_by_apartment, get_requests_summary
)


def test_request_creation():
    """Тест создания заявки."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    request = Request(1, resident, 10, "Ремонт", "Сломалась дверь", False)

    assert request.id == 1
    assert request.resident is resident  # ← проверяем связь!
    assert request.request_type == "Ремонт"
    assert request.status == "Новая"
    assert request.department == "Отдел технического обслуживания"


def test_request_urgent():
    """Тест срочной заявки."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    request = Request(1, resident, 10, "Сантехника", "Течёт кран", True)

    assert request.status == "Срочная"
    assert request.department == "Старший мастер"
    assert request.is_urgent


def test_request_complete():
    """Тест отметки заявки выполненной."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    request = Request(1, resident, 10, "Ремонт", "Описание", False)

    request.complete()
    assert request.status == "Выполнена"
    assert request.is_completed()


def test_request_str():
    """Тест строкового представления."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    request = Request(1, resident, 10, "Ремонт", "Описание", False)

    assert "Ремонт" in str(request)
    assert "Новая" in str(request)


def test_create_request():
    """Тест создания через функцию."""
    residents = [Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")]
    requests = []

    request = create_request(requests, residents[0], 10, "Ремонт", "Описание", False)
    assert len(requests) == 1
    assert request.resident is residents[0]


def test_find_requests_by_apartment():
    """Тест поиска заявок по квартире."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    requests = []
    create_request(requests, resident, 10, "Ремонт", "Описание 1", False)

    found = find_requests_by_apartment(requests, 10)
    assert len(found) == 1


def test_requests_summary():
    """Тест статистики."""
    resident = Resident(1, "Иванов Иван", 10, "+7-999-123-4567", "Собственник")
    requests = []
    create_request(requests, resident, 10, "Ремонт", "Описание 1", False)
    create_request(requests, resident, 20, "Уборка", "Описание 2", True)
    create_request(requests, resident, 30, "Сантехника", "Описание 3", False)

    stats = get_requests_summary(requests)
    assert stats["Всего"] == 3
    assert stats["Срочные"] == 1
    assert stats["Новые"] == 2
