"""
Тесты для модуля requests.py.
"""

from requests import create_request, find_requests_by_apartment, get_requests_summary


def test_create_request():
    """Тест создания заявки."""
    requests_list = []
    request = create_request(requests_list, 1, 10, "Ремонт", "Сломалась дверь", False)
    assert len(requests_list) == 1
    assert request["type"] == "Ремонт"
    assert request["apartment_number"] == 10
    assert request["status"] == "Новая"


def test_create_urgent_request():
    """Тест создания срочной заявки."""
    requests_list = []
    request = create_request(requests_list, 1, 10, "Сантехника", "Течёт кран", True)
    assert request["status"] == "Срочная"
    assert request["department"] == "Старший мастер"


def test_find_requests_by_apartment():
    """Тест поиска заявок по квартире."""
    requests_list = []
    create_request(requests_list, 1, 10, "Ремонт", "Описание 1", False)
    create_request(requests_list, 2, 20, "Уборка", "Описание 2", False)

    found = find_requests_by_apartment(requests_list, 10)
    assert len(found) == 1
    assert found[0]["apartment_number"] == 10


def test_requests_summary():
    """Тест статистики по заявкам."""
    requests_list = []
    create_request(requests_list, 1, 10, "Ремонт", "Описание 1", False)
    create_request(requests_list, 2, 20, "Уборка", "Описание 2", True)
    create_request(requests_list, 3, 30, "Сантехника", "Описание 3", False)

    stats = get_requests_summary(requests_list)
    assert stats["Всего"] == 3
    assert stats["Срочные"] == 1
    assert stats["Новые"] == 3
