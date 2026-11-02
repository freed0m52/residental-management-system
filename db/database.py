import sqlite3
import os


DB_PATH = os.path.join("data", "residents.sqlite")


def get_connection():
    """Создает подключение к базе данных и включает проверку внешних ключей."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
