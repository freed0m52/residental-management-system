"""
Модуль для сохранения и загрузки данных в JSON-файлы.
Преобразует объекты ↔ JSON.
"""

import json
import os
from typing import Any, Dict, List

from models.residents import Resident
from models.requests import Request
from models.premises import Premise
from models.services import Service


def load_data(filename: str) -> List[Dict[str, Any]]:
    """Загрузить данные из JSON-файла."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"⚠️ Ошибка: файл {filename} повреждён.")
        return []
    except Exception as e:
        print(f"⚠️ Ошибка при загрузке {filename}: {e}")
        return []


def save_data(filename: str, data: List[Dict[str, Any]]) -> None:
    """Сохранить данные в JSON-файл."""
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️ Ошибка при сохранении {filename}: {e}")


# ---------- РАБОТА С ЖИТЕЛЯМИ ----------

def load_residents(filename: str) -> List[Resident]:
    """Загрузить жителей из JSON в объекты Resident."""
    data = load_data(filename)
    return [Resident.from_data(d) for d in data]


def save_residents(filename: str, residents: List[Resident]) -> None:
    """Сохранить объекты Resident в JSON."""
    data = [r.to_dict() for r in residents]
    save_data(filename, data)


# ---------- РАБОТА С ЗАЯВКАМИ ----------

def load_requests(
    filename: str,
    residents: List[Resident]
) -> List[Request]:
    """Загрузить заявки из JSON в объекты Request."""
    data = load_data(filename)
    requests = []
    for d in data:
        request = Request.from_data(d, residents)
        if request is not None:
            requests.append(request)
    return requests


def save_requests(filename: str, requests: List[Request]) -> None:
    """Сохранить объекты Request в JSON."""
    data = [r.to_dict() for r in requests]
    save_data(filename, data)


# ---------- РАБОТА С ПОМЕЩЕНИЯМИ ----------

def load_premises(filename: str) -> List[Premise]:
    """Загрузить помещения из JSON."""
    data = load_data(filename)
    return [Premise.from_data(d) for d in data]


def save_premises(filename: str, premises: List[Premise]) -> None:
    """Сохранить помещения в JSON."""
    data = [p.to_dict() for p in premises]
    save_data(filename, data)


# ---------- РАБОТА С УСЛУГАМИ ----------

def load_services(filename: str) -> List[Service]:
    """Загрузить услуги из JSON."""
    data = load_data(filename)
    return [Service.from_data(d) for d in data]


def save_services(filename: str, services: List[Service]) -> None:
    """Сохранить услуги в JSON."""
    data = [s.to_dict() for s in services]
    save_data(filename, data)
