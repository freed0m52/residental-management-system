-- 1. Выборка: Все жители (сортировка по ФИО)
SELECT id, full_name, apartment_number FROM residents ORDER BY full_name;

-- 2. Выборка: Все помещения (сортировка по номеру)
SELECT id, number, premise_type, area FROM premises ORDER BY number;

-- 3. Фильтрация (WHERE): Жители-собственники
SELECT full_name, apartment_number FROM residents WHERE status = 'Собственник';

-- 4. Фильтрация (WHERE): Свободные помещения
SELECT number, area FROM premises WHERE is_occupied = 0;

-- 5. Фильтрация (WHERE + LIKE): Поиск жителя по фамилии
SELECT full_name, phone FROM residents WHERE full_name LIKE '%Иванов%';

-- 6. Агрегатная функция: Общее количество жителей
SELECT COUNT(*) AS total_residents FROM residents;

-- 7. Агрегатная функция: Средняя площадь помещений
SELECT AVG(area) AS avg_area FROM premises;

-- 8. Группировка (GROUP BY): Количество жителей по статусам
SELECT status, COUNT(*) AS count FROM residents GROUP BY status;

-- 9. Группировка (GROUP BY + HAVING): Типы помещений, которых больше одной штуки
SELECT premise_type, COUNT(*) AS count FROM premises GROUP BY premise_type HAVING COUNT(*) > 1;

-- 10. Сложный запрос (JOIN): Список помещений и то, заняты ли они (если бы была связь) - но у нас связи нет, поэтому просто выведем всё вместе.
-- В нашем проекте нет прямой связи жителя и помещения по внешнему ключу, поэтому эмулируем сложный запрос:
SELECT r.full_name, p.number 
FROM residents r, premises p 
WHERE r.apartment_number = p.number;
