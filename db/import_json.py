import json

from db.database import get_connection


RESIDENTS_FILE = "data/residents.json"
PREMISES_FILE = "data/premises.json"


def load_json(filename):
    try:
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []


def import_residents(conn):
    residents = load_json(RESIDENTS_FILE)
    if not residents:
        return

    conn.executemany(
        """
        INSERT INTO residents (id, full_name, apartment_number, phone, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (r["id"], r["full_name"], r["apartment_number"], r["phone"], r["status"])
            for r in residents
        ]
    )


def import_premises(conn):
    premises = load_json(PREMISES_FILE)
    if not premises:
        return

    conn.executemany(
        """
        INSERT INTO premises (id, number, premise_type, area, is_occupied)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (p["id"], p["number"], p["premise_type"], p["area"], int(p["is_occupied"]))
            for p in premises
        ]
    )


def main():
    conn = get_connection()
    try:
        import_residents(conn)
        import_premises(conn)
        conn.commit()
        print("✅ Данные успешно импортированы!")
    except Exception as e:
        conn.rollback()
        print(f"❌ Ошибка импорта: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
