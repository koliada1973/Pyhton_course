# Через API сайту Нацбанку України потрібно отримати курси іноземних валют (долар, євро, фунт) до гривні з початку поточного року. Деталі:
# - для доступу до API використовуйте бібліотеку requests
# - для збереження результатів створіть в базі даних hr (додатковий матеріал до уроків з SQL) дві таблиці. Одна — з полями ’code’ (integer(3), primary key), ’currency’ (varchar(20)), де в першому полі знаходиться код валюти (для долара — 840 і т.д), в другому — назва валюти. В другій таблиці поля id (integer(3), primary key), date (date), value (тип вибрати відповідно до того, як зберігаються дані на сайті Нацбанку), код валюти. Перша таблиця з другою з’єднана відношенням один-до-багатьох по полю code.
# - збережіть дані з сайту в новостворені таблиці в БД
# - виведіть середнє значення курсу по кожній валюті, використовуючи group by
# - виведіть графік курсу валют (використовуючи відповідну бібліотеку, з допомогою якої раніше малювали фігури)
# - постарайтесь всі завдання виконати суто з python (в т.ч. операції з БД)


import requests
import sqlite3

conn = sqlite3.connect("hr.db")
cursor = conn.cursor()

# Створення таблиць currency_1 та currency_2
cursor.execute("""
CREATE TABLE IF NOT EXISTS currency_1 (
    code integer primary key,
    currency varchar(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS currency_2 (
    id integer primary key AUTOINCREMENT,
    date date,
    value real,
    currency_cod integer,
    FOREIGN KEY (currency_cod) REFERENCES currency_1(code)
)
""")
conn.commit()

# Видаляємо дані, якщо вони вже були:
cursor.execute("DELETE FROM currency_1")
conn.commit()

cursor.execute("DELETE FROM currency_2")
conn.commit()

"""
r030":840,"cc":"USD"
r030":978,"cc":"EUR"
r030":826,"cc":"GBP
"""
cursor.execute("INSERT INTO currency_1 (code, currency) VALUES (?, ?)", (840, 'USD'))
cursor.execute("INSERT INTO currency_1 (code, currency) VALUES (?, ?)", (978, 'EUR'))
cursor.execute("INSERT INTO currency_1 (code, currency) VALUES (?, ?)", (826, 'GBP'))
conn.commit()


url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250101&end=20250920&sort=exchangedate&order=asc&json"
response = requests.get(url)

for item in response.json():
    cursor.execute("INSERT INTO currency_2 (date, value, currency_cod) VALUES (?, ?, ?)", (item['exchangedate'], item['rate'], item['r030']))
conn.commit()

# cursor.execute("SELECT avg(c.value) FROM currency_2 c WHERE c.currency_cod = 840 GROUP BY c.currency_cod;")
# avg_curr = cursor.fetchone()[0]
# print(f"Середнє значення курсу: {avg_curr}")


# Дані
cursor.execute("SELECT DISTINCT date FROM currency_2;")
dates = cursor.fetchall()
dates = [row[0] for row in dates]

cursor.execute("SELECT value FROM currency_2 WHERE currency_cod = 840  ORDER BY date ASC;")
value1 = cursor.fetchall()
USD = [row[0] for row in value1]

cursor.execute("SELECT value FROM currency_2 WHERE currency_cod = 826 ORDER BY date ASC;")
value2 = cursor.fetchall()
EUR = [row[0] for row in value2]

cursor.execute("SELECT value FROM currency_2 WHERE currency_cod = 978 ORDER BY date ASC;")
value3 = cursor.fetchall()
GBR = [row[0] for row in value3]











import turtle

# Налаштування екрану
screen = turtle.Screen()
screen.setup(900, 600)
screen.title("Курс USD, EUR, GBR по датам")

t = turtle.Turtle()
t.speed(0)

# --- Малюємо осі ---
t.penup()
t.goto(-350, -200)
t.pendown()
t.forward(700)  # X-вісь (дати)

t.penup()
t.goto(-350, -200)
t.left(90)
t.pendown()
t.forward(450)  # Y-вісь (value)
t.penup()
#
# --- Функція для малювання однієї лінії ---
def draw_line(values, color):
    t.penup()
    t.color(color)
    x_step = 2  # відстань між датами по X
    y_scale = 5   # масштаб для значень
    for i, value in enumerate(values):
        x = -350 + i * x_step
        y = -200 + value * y_scale
        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
    t.penup()

# --- Малюємо три графіки ---
draw_line(USD, "red")
draw_line(EUR, "blue")
draw_line(GBR, "green")

# Підписи дат на осі X (місяці)
from datetime import datetime

t.color("black")
for i, date in enumerate(dates):
    d = datetime.strptime(date, "%d.%m.%Y")
    if d.day == 1:
        x = -350 + i * 2
        t.goto(x, -220)
        t.write(d.month, align="center", font=("Arial", 10, "normal"))

# --- Підписи значень на осі Y ---
for v in range(0, int(max(USD + EUR + GBR)) + 10, 10):  # for v in range(0, max(value1 + value2 + value3) + 10, 10):
    y = -200 + v * 5
    t.goto(-370, y)
    t.write(str(v), align="right", font=("Arial", 10, "normal"))

# --- Легенда ---
t.goto(200, 180); t.color("red");   t.write("USD", font=("Arial", 10, "normal"))
t.goto(200, 160); t.color("blue");  t.write("EUR", font=("Arial", 10, "normal"))
t.goto(200, 140); t.color("green"); t.write("GBR", font=("Arial", 10, "normal"))
#
turtle.done()