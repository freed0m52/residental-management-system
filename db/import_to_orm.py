import os
import sys
import sqlite3
from pathlib import Path
import django

# Настройка путей
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
SOURCE_DB = BASE_DIR / "data" / "residents.sqlite"

# Инициализация Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roomly.settings")
django.setup()

# Импорт моделей
from residents.models import Resident
from premises.models import Premise


def main():
    if not SOURCE_DB.exists():
        print("❌ Исходная база не найдена!")
        return

    with sqlite3.connect(SOURCE_DB) as conn:
        conn.row_factory = sqlite3.Row

        # Переносим жителей
        residents = conn.execute("SELECT * FROM residents").fetchall()
        for row in residents:
            Resident.objects.update_or_create(
                id=row["id"],
                defaults={
                    "full_name": row["full_name"],
                    "apartment_number": row["apartment_number"],
                    "phone": row["phone"],
                    "status": row["status"],
                }
            )

        # Переносим помещения
        premises = conn.execute("SELECT * FROM premises").fetchall()
        for row in premises:
            Premise.objects.update_or_create(
                id=row["id"],
                defaults={
                    "number": row["number"],
                    "premise_type": row["premise_type"],
                    "area": row["area"],
                    "is_occupied": bool(row["is_occupied"]),
                }
            )

    print("✅ Данные успешно перенесены в ORM!")
    print(f"Жителей: {Resident.objects.count()}")
    print(f"Помещений: {Premise.objects.count()}")


if __name__ == "__main__":
    main()
