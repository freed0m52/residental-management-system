import json
import os
from typing import Any, Dict, List


def load_data(filename: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} повреждён. Создан новый.")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке {filename}: {e}")
        return []


def save_data(filename: str, data: List[Dict[str, Any]]) -> None:
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка при сохранении {filename}: {e}")
