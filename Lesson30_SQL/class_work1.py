# Задача 1.
# ·      створити таблицю для працівників, з стовбцями: id, first_name, last_name, department, salary
# ·      змінити таблицю, додавши ще один стовпець - date
# ·      перейменувати даний стовпець на hire_date
# ·      перейменувати таблицю на new_employee
# ·      додати в таблицю запис про працівника
# ·      очистити таблицю
# ·      видалити таблицю

"""
CREATE Table Workers (
    id int PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department VARCHAR(255),
    salary int);

ALTER TABLE Workers
    ADD COLUMN Date DATE;

ALTER TABLE Workers
    RENAME COLUMN Date TO Hire_Date;

ALTER TABLE Workers
    RENAME TO new_employee;

INSERT INTO new_employee (id, first_name, last_name, department, salary, Hire_Date)
VALUES (1,'Vasya', 'Petrenko', 'IT', 100000, '2025-08-10');

DROP TABLE new_employee;
"""