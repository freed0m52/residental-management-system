"""
Система управления жилым комплексом.
Главный модуль — точка входа в приложение.
"""

import os
from typing import List, Dict, Any

from utils import input_int
from storage import load_data, save_data
from residents import (
    add_resident,
    find_resident_by_name,
    find_resident_by_apartment,
    sort_residents_by_name
)
from requests import (
    create_request,
    find_requests_by_apartment,
    find_requests_by_status,
    get_requests_summary,
    REQUEST_TYPES
)

# Пути к файлам данных
DATA_DIR = "data"
RESIDENTS_FILE = os.path.join(DATA_DIR, "residents.json")
REQUESTS_FILE = os.path.join(DATA_DIR, "requests.json")


def load_all_data() -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Загрузить все данные из JSON-файлов."""
    residents = load_data(RESIDENTS_FILE)
    requests = load_data(REQUESTS_FILE)
    return residents, requests


def save_all_data(residents: List[Dict[str, Any]], requests: List[Dict[str, Any]]) -> None:
    """Сохранить все данные в JSON-файлы."""
    save_data(RESIDENTS_FILE, residents)
    save_data(REQUESTS_FILE, requests)


def show_residents(residents: List[Dict[str, Any]]) -> None:
    """Вывести список всех жителей."""
    if not residents:
        print("\n📋 Список жителей пуст.")
        return

    print("\n" + "=" * 60)
    print("📋 СПИСОК ЖИТЕЛЕЙ")
    print("=" * 60)

    sorted_residents = sort_residents_by_name(residents)

    for r in sorted_residents:
        print(f"ID: {r['id']}")
        print(f"  ФИО: {r['full_name']}")
        print(f"  Квартира: {r['apartment_number']}")
        print(f"  Телефон: {r['phone']}")
        print(f"  Статус: {r['status']}")
        print("-" * 40)


def show_requests(requests: List[Dict[str, Any]]) -> None:
    """Вывести список всех заявок."""
    if not requests:
        print("\n📋 Список заявок пуст.")
        return

    print("\n" + "=" * 60)
    print("📋 СПИСОК ЗАЯВОК")
    print("=" * 60)

    for r in requests:
        urgent = "⚠️ СРОЧНО" if r.get("is_urgent", False) else ""
        print(f"ID: {r['id']} {urgent}")
        print(f"  Квартира: {r['apartment_number']}")
        print(f"  Тип: {r['type']}")
        print(f"  Описание: {r['description']}")
        print(f"  Статус: {r['status']}")
        print(f"  Отдел: {r['department']}")
        print(f"  Дата: {r['created_at']}")
        print("-" * 40)


def show_statistics(requests: List[Dict[str, Any]]) -> None:
    """Вывести статистику по заявкам."""
    stats = get_requests_summary(requests)

    print("\n" + "=" * 60)
    print("📊 СТАТИСТИКА ЗАЯВОК")
    print("=" * 60)
    print(f"Всего заявок: {stats['Всего']}")
    print(f"Новые: {stats['Новые']}")
    print(f"Срочные: {stats['Срочные']}")
    print(f"Выполненные: {stats['Выполненные']}")


def main() -> None:
    """Главная функция приложения."""
    print("\n" + "=" * 60)
    print("🏢 СИСТЕМА УПРАВЛЕНИЯ ЖИЛЫМ КОМПЛЕКСОМ")
    print("=" * 60)

    # Загрузка данных
    residents, requests = load_all_data()
    print(f"✅ Загружено жителей: {len(residents)}")
    print(f"✅ Загружено заявок: {len(requests)}")

    while True:
        print("\n" + "-" * 40)
        print("МЕНЮ:")
        print("  1. Показать всех жителей")
        print("  2. Добавить жителя")
        print("  3. Найти жителя по квартире")
        print("  4. Найти жителя по ФИО")
        print("  5. Показать все заявки")
        print("  6. Создать заявку")
        print("  7. Найти заявки по квартире")
        print("  8. Найти заявки по статусу")
        print("  9. Показать статистику")
        print("  0. Выход")
        print("-" * 40)

        choice = input_int("Выберите действие: ")

        if choice == 0:
            print("💾 Сохраняем данные...")
            save_all_data(residents, requests)
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
            print(f"✅ Житель добавлен! ID: {resident['id']}")

        elif choice == 3:
            apartment = input_int("Введите номер квартиры: ")
            resident = find_resident_by_apartment(residents, apartment)
            if resident:
                print(f"\n✅ Найден: {resident['full_name']}")
                print(f"   Телефон: {resident['phone']}")
                print(f"   Статус: {resident['status']}")
            else:
                print(f"❌ Житель в квартире {apartment} не найден.")

        elif choice == 4:
            query = input("Введите ФИО или часть ФИО: ").strip()
            found = find_resident_by_name(residents, query)
            if found:
                print(f"\n✅ Найдено {len(found)} жителей:")
                for r in found:
                    print(f"  - {r['full_name']} (кв. {r['apartment_number']})")
            else:
                print("❌ Ничего не найдено.")

        elif choice == 5:
            show_requests(requests)

        elif choice == 6:
            print("\n➕ СОЗДАНИЕ ЗАЯВКИ")
            apartment = input_int("  Номер квартиры: ")

            resident = find_resident_by_apartment(residents, apartment)
            if not resident:
                print("❌ Житель с такой квартирой не найден. Сначала зарегистрируйте жителя.")
                continue

            print("  Тип заявки:")
            for key, value in REQUEST_TYPES.items():
                print(f"    {key}. {value}")
            type_choice = input("  Выберите тип (1-3): ").strip()
            request_type = REQUEST_TYPES.get(type_choice, "Другое")

            description = input("  Описание проблемы: ").strip()
            urgent_choice = input("  Срочная? (1 - да, 2 - нет): ").strip()
            is_urgent = urgent_choice == "1"

            request = create_request(
                requests,
                resident["id"],
                apartment,
                request_type,
                description,
                is_urgent
            )
            print(f"✅ Заявка создана! ID: {request['id']}")
            print(f"   Отдел: {request['department']}")

        elif choice == 7:
            apartment = input_int("Введите номер квартиры: ")
            found = find_requests_by_apartment(requests, apartment)
            if found:
                print(f"\n✅ Найдено {len(found)} заявок:")
                for r in found:
                    urgent = "⚠️ " if r.get("is_urgent", False) else ""
                    print(f"  {urgent}ID {r['id']}: {r['type']} - {r['status']}")
            else:
                print(f"❌ Заявок для квартиры {apartment} не найдено.")

        elif choice == 8:
            status = input("Введите статус (Новая/Выполнена): ").strip()
            found = find_requests_by_status(requests, status)
            if found:
                print(f"\n✅ Найдено {len(found)} заявок со статусом '{status}':")
                for r in found:
                    print(f"  - ID {r['id']}: кв. {r['apartment_number']}, {r['type']}")
            else:
                print(f"❌ Заявок со статусом '{status}' не найдено.")

        elif choice == 9:
            show_statistics(requests)

        else:
            print("❌ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
