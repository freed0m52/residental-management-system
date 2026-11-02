-- Структура базы данных проекта
CREATE TABLE IF NOT EXISTS residents (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    apartment_number INTEGER NOT NULL,
    phone TEXT,
    status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS premises (
    id INTEGER PRIMARY KEY,
    number INTEGER NOT NULL,
    premise_type TEXT NOT NULL,
    area REAL NOT NULL,
    is_occupied INTEGER NOT NULL DEFAULT 0
);
