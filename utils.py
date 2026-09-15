from datetime import datetime


def input_int(prompt: str) -> int:
    """
    Запросить у пользователя целое число.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date(prompt: str) -> str:
    """
    Запросить у пользователя дату в формате ДД.ММ.ГГГГ.
    """
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
            return date_str
        except ValueError:
            print("Ошибка: введите дату в формате ДД.ММ.ГГГГ")


def generate_id() -> int:
    """
    Сгенерировать уникальный идентификатор.
    """
    return int(datetime.now().timestamp() * 1000) % 1000000
