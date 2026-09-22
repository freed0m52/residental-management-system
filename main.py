"""
Система управления жилым комплексом.
Главный модуль — точка входа в приложение.
"""

import os
from typing import List

from utils import input_int
from storage import (
    load_residents, save_residents,
    load_requests, save_requests,
    load_premises, save_premises,
    load_services, save_services
)
from models.residents import (
    Resident, add_resident, find_resident_by_apartment, show_residents
)
from models.requests import (
    Request, create_request, get_requests_summary,
    show_requests, REQUEST_TYPES
)
from models.premises import add_premise, show_premises
from models.services import add_service, show_services

# Пути к файлам данных
DATA_DIR = "data"
RESIDENTS_FILE = os.path.join(DATA_DIR, "residents.json")
REQUESTS_FILE = os.path.join(DATA_DIR, "requests.json")
PREMISES_FILE = os.path.join(DATA_DIR, "premises.json")
SERVICES_FILE = os.path.join(DATA_DIR, "services.json")


def show_statistics(requests: List[Request]) -> None:
    """Вывести статистику по заявкам."""
    stats = get_requests_summary(requests)

    print("\n" + "=" * 60)
    print("📊 СТАТИСТИКА ЗАЯВОК")
    print("=" * 60)
    print(f"Всего заявок: {stats['Всего']}")
    print(f"Новые: {stats['Новые']}")
    print(f"Срочные: {stats['Срочные']}")
    print(f"Выполненные: {stats['Выполненные']}")


def create_new_request(
    requests: List[Request],
    residents: List[Resident]
) -> None:
    """Создать заявку через меню."""
    print("\n➕ СОЗДАНИЕ ЗАЯВКИ")
    apartment = input_int("  Номер квартиры: ")

    resident = find_resident_by_apartment(residents, apartment)
    if resident is None:
        print("❌ Житель с такой квартирой не найден.")
        return

    print("  Тип заявки:")
    for key, value in REQUEST_TYPES.items():
        print(f"    {key}. {value}")

    type_choice = input("  Выберите тип (1-3): ").strip()
    request_type = REQUEST_TYPES.get(type_choice, "Другое")

    description = input("  Описание проблемы: ").strip()
    urgent = input("  Срочная? (1 - да, 2 - нет): ").strip() == "1"

    request = create_request(
        requests, resident, apartment, request_type, description, urgent
    )
    print(f"✅ Заявка создана! ID: {request.id}")
    print(f"   Отдел: {request.department}")


def main() -> None:
    """Главная функция приложения."""
    print("\n" + "=" * 60)
    print("🏢 СИСТЕМА УПРАВЛЕНИЯ ЖИЛЫМ КОМПЛЕКСОМ")
    print("=" * 60)

    # Загрузка объектов
    residents = load_residents(RESIDENTS_FILE)
    requests = load_requests(REQUESTS_FILE, residents)
    premises = load_premises(PREMISES_FILE)
    services = load_services(SERVICES_FILE)

    print(f"✅ Жителей: {len(residents)}")
    print(f"✅ Заявок: {len(requests)}")
    print(f"✅ Помещений: {len(premises)}")
    print(f"✅ Услуг: {len(services)}")

    while True:
        print("\n" + "-" * 40)
        print("МЕНЮ:")
        print("  1. Показать всех жителей")
        print("  2. Добавить жителя")
        print("  3. Показать все заявки")
        print("  4. Создать заявку")
        print("  5. Показать все помещения")
        print("  6. Добавить помещение")
        print("  7. Показать все услуги")
        print("  8. Добавить услугу")
        print("  9. Статистика заявок")
        print("  0. Выход")
        print("-" * 40)

        choice = input_int("Выберите действие: ")

        if choice == 0:
            print("💾 Сохраняем данные...")
            save_residents(RESIDENTS_FILE, residents)
            save_requests(REQUESTS_FILE, requests)
            save_premises(PREMISES_FILE, premises)
            save_services(SERVICES_FILE, services)
            print("👋 До свидания!")
            break

        elif choice == 1:
            show_residents(residents)

        elif choice == 2:
            print("\n➕ ДОБАВЛЕНИЕ ЖИТЕЛЯ")
            full_name = input("  ФИО: ").strip()
            apartment = input_int("  Номер квартиры: ")
            phone = input("  Телефон: ").strip()
            status_choice = input("  Статус (1 - Собственник, 2 - Арендатор): ").strip()
            status = "Собственник" if status_choice == "1" else "Арендатор"

            resident = add_resident(residents, full_name, apartment, phone, status)
            print(f"✅ Житель добавлен! ID: {resident.id}")

        elif choice == 3:
            show_requests(requests)

        elif choice == 4:
            create_new_request(requests, residents)

        elif choice == 5:
            show_premises(premises)

        elif choice == 6:
            print("\n➕ ДОБАВЛЕНИЕ ПОМЕЩЕНИЯ")
            number = input_int("  Номер помещения: ")
            type_choice = input("  Тип (1 - Жилое, 2 - Коммерческое): ").strip()
            ptype = "Жилое" if type_choice == "1" else "Коммерческое"
            area = float(input("  Площадь (кв.м): ").strip())

            premise = add_premise(premises, number, ptype, area)
            print(f"✅ Помещение добавлено! ID: {premise.id}")

        elif choice == 7:
            show_services(services)

        elif choice == 8:
            print("\n➕ ДОБАВЛЕНИЕ УСЛУГИ")
            name = input("  Название: ").strip()
            cost = float(input("  Стоимость: ").strip())
            period_choice = input("  Периодичность (1 - Ежемесячно, 2 - Разово): ").strip()
            period = "Ежемесячно" if period_choice == "1" else "Разово"

            service = add_service(services, name, cost, period)
            print(f"✅ Услуга добавлена! ID: {service.id}")

        elif choice == 9:
            show_statistics(requests)

        else:
            print("❌ Неверный выбор.")


if __name__ == "__main__":
    main()
