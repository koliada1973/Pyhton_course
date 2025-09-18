-- Class_work1
-- Знайти імена співробітників та назви їхніх відділів
SELECT e.first_name || ' ' || e.last_name AS full_name, d.depart_name
FROM employees e JOIN departments d ON e.department_id = d.department_id;

-- Завдання 2 (LEFT JOIN)
-- Вивести всі відділи й менеджерів, навіть якщо у відділі немає працівників.
SELECT d.depart_name, e.first_name || ' ' || e.last_name AS manager_name
FROM departments d LEFT JOIN employees e ON d.manager_id = employee_id;

-- Завдання 3 (RIGHT JOIN — у SQLite треба імітувати через LEFT JOIN)
-- Знайти всіх співробітників і відділи, навіть якщо співробітник не має department_id.
SELECT e.first_name || ' ' || e.last_name AS full_name, d.depart_name
FROM departments d LEFT JOIN employees e ON e.department_id = d.department_id;

-- Завдання 4 (CROSS JOIN) - забув про нього розповісти )
-- Зробити декартів добуток між таблицею regions і countries.
SELECT *
FROM regions CROSS JOIN countries;

-- Завдання 5 (subquery у WHERE)
-- Знайти співробітників, чия зарплата більша за середню.
SELECT e.first_name || ' ' || e.last_name AS full_name
FROM employees e
WHERE salary > (SELECT AVG(salary) as AVG_salary FROM employees);

-- Завдання 6 (subquery у FROM)
-- Вивести середню зарплату по кожному відділу.
SELECT depart_name, tab.AVG_salery
FROM (SELECT d.depart_name, AVG(e.salary) as AVG_salery
        FROM employees e JOIN departments d ON e.department_id = d.department_id
        GROUP BY e.department_id) as tab;

-- Завдання 7 (correlated subquery)
-- Знайти співробітників, які отримують найвищу зарплату у своєму відділі.
SELECT e.first_name || ' ' || e.last_name AS full_name, e.salary, d.depart_name
FROM employees e JOIN departments d ON e.department_id = d.department_id
WHERE e.salary in (SELECT max(e.salary)
FROM employees e
GROUP BY department_id)
GROUP BY e.department_id;

-- Завдання 8 (простий GROUP BY)
-- Порахувати кількість співробітників у кожному відділі.
SELECT  d.depart_name,count(*)  AS count_employees
FROM employees e JOIN departments d ON e.department_id = d.department_id
GROUP BY e.department_id;

-- Завдання 9 (GROUP BY з HAVING)
-- Знайти відділи, де середня зарплата > 8000
SELECT  d.depart_name, AVG(e.salary) AS avg_salary
FROM departments d JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id
HAVING AVG(e.salary) > 8000;

-- Завдання 10 (GROUP BY з кількома полями)
-- Порахувати кількість співробітників по кожній посаді в кожному відділі.
SELECT d.depart_name, e.job_id, count(*)
FROM employees e JOIN departments d ON d.department_id = e.department_id
GROUP BY d.depart_name, e.job_id
ORDER BY d.depart_name, e.job_id;

-- Додаткові завдання, опційні (більш складні), для любителів помучитись після уроків )):
-- INNER JOIN (складніший)
-- Задача: Знайти співробітників, їхні відділи, офіси (місто) та країни, де вони працюють.
SELECT e.first_name || ' ' || e.last_name AS full_name, d.depart_name, l.city, c.country_name
FROM employees e
    JOIN departments d on e.department_id = d.department_id
    JOIN locations l ON d.location_id = l.location_id
    JOIN countries c on l.country_id = c.country_id;

-- LEFT JOIN (складніший)
-- Задача: Вивести всі відділи та кількість співробітників у них. Якщо співробітників немає, показати 0.
SELECT d.depart_name, IFNULL(COUNT(e.employee_id), 0) AS count_employees
FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.depart_name;

-- RIGHT JOIN (імітація через LEFT JOIN)
-- Задача: Показати всіх співробітників і назву відділу, навіть якщо відділу немає (тобто department_id = NULL).
SELECT e.first_name || ' ' || e.last_name AS full_name, d.depart_name
FROM employees e
    LEFT JOIN departments d on e.department_id = d.department_id;

-- FULL OUTER JOIN (імітація через UNION)
-- Задача: Показати всі department_id і всіх employee_id, навіть якщо немає збігів.
SELECT d.department_id,e.employee_id
FROM employees e
    LEFT JOIN departments d ON d.department_id = e.department_id
UNION
SELECT d.department_id, e.employee_id
FROM departments d
    LEFT JOIN employees e ON d.department_id = e.department_id;

-- CROSS JOIN (складніший)
-- Задача: Створити всі можливі пари «співробітник – робота (job)», щоб подивитися, які комбінації могли б існувати.
SELECT e.first_name || ' ' || e.last_name AS full_name, j.job_title
FROM employees e CROSS JOIN jobs j;

-- 2. Комбіновані задачі (JOIN + GROUP BY + SUBQUERY)
-- Завдання 1
-- Знайти відділ із найбільшою кількістю співробітників.
SELECT depart_name, MAX(count_employees)
FROM (SELECT d.depart_name, COUNT(e.employee_id) as count_employees
    FROM departments d
        LEFT JOIN employees e ON d.department_id = e.department_id
    GROUP BY d.department_id) t1;

-- Завдання 2
-- Знайти співробітників, які заробляють більше за середню зарплату у своєму відділі.

SELECT d.depart_name,
       e.first_name || ' ' || e.last_name AS full_name,
       e.salary
FROM employees e
    JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e.department_id = e2.department_id --department_id порівнюються в обох таблицях e2 та e
    );

-- Завдання 3
-- Порахувати середню зарплату по кожній країні.
SELECT c.country_name, AVG(e.salary) AS avg_salary
FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    JOIN locations l ON d.location_id = l.location_id
    JOIN countries c ON l.country_id = c.country_id
GROUP BY c.country_name;

-- Завдання 4
-- Знайти топ-3 співробітників із найвищою зарплатою в кожному відділі.
SELECT d.depart_name,
       e1.first_name || ' ' || e1.last_name AS full_name,
       e1.salary
FROM employees e1 JOIN departments d ON e1.department_id = d.department_id
WHERE (
    SELECT COUNT(*)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
      AND e2.salary > e1.salary
) < 3
ORDER BY e1.department_id, e1.salary DESC;

-- Завдання 5
-- Знайти країну, де працює найбільше співробітників.
SELECT country_name, MAX(count_emp) AS count_employees
FROM (SELECT c.country_name, count(e.employee_id) as count_emp
    FROM employees e
        JOIN departments d ON e.department_id = d.department_id
        JOIN locations l ON d.location_id = l.location_id
        JOIN countries c ON l.country_id = c.country_id
    GROUP BY c.country_name);