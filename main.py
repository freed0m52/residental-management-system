import datetime

def get_apartment_status(status_choice):
    if status_choice == "1":
        return "Собственник"
    elif status_choice == "2":
        return "Арендатор"
    else:
        print("Некорректный выбор статуса. Установлено значение 'Неизвестно'.")
        return "Неизвестно"

def get_request_type(request_choice):
    if request_choice == "1":
        return "Ремонт"
    elif request_choice == "2":
        return "Уборка"
    elif request_choice == "3":
        return "Сантехника"
    else:
        print("Выбран неизвестный тип заявки. Установлено 'Другое'.")
        return "Другое"

def get_request_status(urgency_choice):
    if urgency_choice == "2":
        print("Заявка помечена как срочная!")
        return "Срочная (в обработке)"
    else:
        return "Новая"

def generate_request_number(apartment_number):
    current_date = datetime.datetime.now()
    return current_date.strftime("%Y%m%d") + str(apartment_number)

def get_department(request_type, request_status):
    if request_status == "Срочная (в обработке)":
        return "Старший мастер"
    elif request_type in ("Сантехника", "Ремонт"):
        return "Отдел технического обслуживания"
    else:
        return "Общий отдел"


def print_resident_info(full_name, apartment_number, phone, status):
    print(f"\nЖитель {full_name} успешно зарегистрирован!")
    print(f"   Квартира: {apartment_number}")
    print(f"   Телефон: {phone}")
    print(f"   Статус: {status}")

def print_request_info(request_number, full_name, request_type, description, request_status):
    print("\nСоздана новая заявка")
    print(f"Номер заявки: {request_number}")
    print(f"Житель: {full_name}")
    print(f"Тип: {request_type}")
    print(f"Описание: {description}")
    print(f"Статус: {request_status}")
    print(f"Дата: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}")

def print_department_info(department):
    if department == "Старший мастер":
        print(f"\nСрочная заявка направлена {department}.")
    elif department == "Отдел технического обслуживания":
        print(f"\nЗаявка направлена в {department}.")
    else:
        print(f"\nЗаявка направлена в {department}.")

def print_summary(is_registered, request_number):
    print("\nИТОГО")
    registration_status = "Успешно" if not is_registered else "Пропущена"
    print(f"Регистрация: {registration_status}")
    print(f"Заявка №{request_number} создана")

def main():
    
    print("Регистрация нового жителя")
    
    full_name = input("Введите ФИО жителя: ")
    apartment_number = int(input("Введите номер квартиры: "))
    phone = input("Введите контактный телефон: ")
    
    status_choice = input("Статус проживания (1 - собственник, 2 - арендатор): ")
    status = get_apartment_status(status_choice)
    
    is_registered = False
    
    if is_registered:
        print(f"\nЖитель {full_name} уже зарегистрирован в системе.")
    else:
        print_resident_info(full_name, apartment_number, phone, status)
    
    print("\nПодача заявки на обслуживание")
    request_choice = input("Выберите тип заявки (1 - ремонт, 2 - уборка, 3 - сантехника): ")
    request_type = get_request_type(request_choice)
    
    description = input("Краткое описание проблемы: ")
    
    urgency_choice = input("Срочность заявки (1 - обычная, 2 - срочная): ")
    request_status = get_request_status(urgency_choice)
    
    request_number = generate_request_number(apartment_number)
    
    print_request_info(request_number, full_name, request_type, description, request_status)
    
    department = get_department(request_type, request_status)
    print_department_info(department)
    
    print_summary(is_registered, request_number)

if __name__ == "__main__":
    main()