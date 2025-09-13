# Задача 3.
# ·      Створити повну копію таблиці employee, використовуючи SELECT
# ·      зробіть вибірку з таблиці employee з допомогою SELECT використовуючи LIKE, EXISTS, BETWEEN оператори (не одночасно)
# ·      зробіть вибірку з employee first_name, last_name, department, salary , сортування по department ASC, по salary – DESC

"""
Створити повну копію таблиці employee, використовуючи SELECT:
CREATE TABLE employee2 AS SELECT * FROM employees;

зробіть вибірку з таблиці employee з допомогою SELECT використовуючи LIKE, EXISTS, BETWEEN оператори (не одночасно):
SELECT *
FROM employees
WHERE last_name LIKE 'A%';

оператор EXISTS використовується для перевірки, чи повертає підзапит хоча б один рядок:
SELECT *
FROM employees
WHERE EXISTS (SELECT 1 FROM main.employees WHERE salary > 10000);
у EXISTS зазвичай пишуть SELECT 1, бо самі дані з підзапиту не важливі
— важливий лише факт існування рядка

SELECT *
FROM employees
WHERE salary BETWEEN 15000 and 30000;

зробіть вибірку з employee first_name, last_name, department, salary ,
сортування по department ASC, по salary – DESC
SELECT first_name, last_name, department_id, salary FROM employees ORDER BY department_id, salary desc;
"""