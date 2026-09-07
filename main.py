import datetime

print("Регистрация нового жителя")
full_name = input("Введите ФИО жителя: ")
apartment_number = int(input("Введите номер квартиры: "))
phone = input("Введите контактный телефон: ")
status_choice = input("Статус проживания (1 - собственник, 2 - арендатор): ")

if status_choice == "1":
    status = "Собственник"
elif status_choice == "2":
    status = "Арендатор"
else:
    status = "Неизвестно"
    print("Некорректный выбор статуса. Установлено значение 'Неизвестно'.")
is_registered = False

if is_registered:
    print(f"\nЖитель {full_name} уже зарегистрирован в системе.")
else:
    print(f"\nЖитель {full_name} успешно зарегистрирован!")
    print(f"Квартира: {apartment_number}")
    print(f"Телефон: {phone}")
    print(f"Статус: {status}")

print("\nПодача заявки на обслуживание")
request_choice = input("Выберите тип заявки (1 - ремонт, 2 - уборка, 3 - сантехника): ")

if request_choice == "1":
    request_type = "Ремонт"
elif request_choice == "2":
    request_type = "Уборка"
elif request_choice == "3":
    request_type = "Сантехника"
else:
    request_type = "Другое"
    print("Выбран неизвестный тип заявки. Установлено 'Другое'.")

description = input("Краткое описание проблемы: ")

current_date = datetime.datetime.now()
request_number = current_date.strftime("%Y%m%d") + str(apartment_number)

status_auto_choice = input("Срочность заявки (1 - обычная, 2 - срочная): ")
if status_auto_choice == "2":
    request_status = "Срочная (в обработке)"
    print("Заявка помечена как срочная!")
else:
    request_status = "Новая"

print("\nСоздана новая заявка")
print(f"Номер заявки: {request_number}")
print(f"Житель: {full_name}")
print(f"Тип: {request_type}")
print(f"Описание: {description}")
print(f"Статус: {request_status}")
print(f"Дата создания: {current_date.strftime('%d.%m.%Y %H:%M')}")

if request_status == "Срочная (в обработке)":
    print("\nСрочная заявка направлена старшему мастеру.")
elif request_type == "Сантехника" or request_type == "Ремонт":
    print("\nЗаявка направлена в отдел технического обслуживания.")
else:
    print("\nЗаявка направлена в общий отдел.")

print("\nИТОГОВАЯ ИНФОРМАЦИЯ ")
print(f"Регистрация жителя: {'Успешно' if not is_registered else 'Пропущена'}")
print(f"Создана заявка: {request_number}")
print("Спасибо, что пользуетесь нашей системой!")