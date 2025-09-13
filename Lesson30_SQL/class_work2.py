# Задача 2.
# ·      створити таблицю, згідно пункту 1.1
# ·      додати кілька працівників
# ·      додати кілька працівників, що працюють в одному департаменті (ІТ)
# ·      підняти зарплату ІТ-шникам на 20% (update)
# ·      звільнити всіх, крім ІТ-шників (DELETE)
# ·      звільнити всіх (TRUNCATE)
# ·      стартап закрито (видалити таблицю) - обережно з стартапами, тримайтесь подалі від них, 97 з 100 закриваються )

"""
Задача 2.
створити таблицю, згідно пункту 1.1:
CREATE Table Workers (
    id int PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department VARCHAR(255),
    salary int);

додати кілька працівників:
INSERT INTO Workers (id, first_name, last_name, department, salary)
VALUES (1, 'Petro', 'Sidorov', 'HR', 30000),
       (2,'Ivan', 'Petrenko', 'Marketing', 25000),
       (3, 'Oleksandr', 'Ivanov', 'Finance', 45000);

додати кілька працівників, що працюють в одному департаменті (ІТ):
INSERT INTO Workers (id, first_name, last_name, department, salary)
VALUES (4, 'Bogdan', 'Pidgorny', 'IT', 30000),
       (5,'Stepan', 'Shmatko', 'IT', 25000);

підняти зарплату ІТ-шникам на 20% (update):
UPDATE Workers SET salary = Workers.salary * 1.2 WHERE department = 'IT';

звільнити всіх, крім ІТ-шників (DELETE):
DELETE FROM Workers
WHERE NOT department = 'IT';

звільнити всіх (TRUNCATE):
У SQLite немає TRUNCATE TABLE, тому використовують саме DELETE
DELETE FROM Workers;

стартап закрито (видалити таблицю):
DROP TABLE Workers;
"""