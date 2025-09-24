import requests

import sqlite3

connection = sqlite3.connect('hr.db')
cursor = connection.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS currency_1 (
#     code INTEGER PRIMARY KEY,
#     currency VARCHAR(20)
# )
# ''')
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS currency_2 (
#     id INTEGER PRIMARY KEY AUTOINCREMENT ,
#     date DATE,
#     value DECIMAL,
#     currency_code INTEGER,
#     FOREIGN KEY (currency_code) REFERENCES currency_1(code)
#
# )
# ''')

# connection.commit()

# response_all = requests.get('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250101&end=20250920&sort=exchangedate&order=asc&json')

#
# print(response.json())
#
# cursor.execute(
#     "INSERT INTO currency_1 (code, currency) VALUES (?, ?)",
#     (840, "USD"))
# cursor.execute(
#     "INSERT INTO currency_1 (code, currency) VALUES (?, ?)",
#     (978, "EUR"))
# cursor.execute(
#     "INSERT INTO currency_1 (code, currency) VALUES (?, ?)",
#     (826, "GBR"))
# connection.commit()

# for item in response_all.json():
#     # Додавання одного рядка
#     cursor.execute(f"INSERT INTO currency_2 (date, value,  currency_code) VALUES (?, ?, ?)", (
#         item['exchangedate'],
#         item['rate'],
#         item['r030']
#     ))
# connection.commit()

# USD
cursor.execute("SELECT AVG(value), currency_code FROM currency_2 WHERE currency_2.currency_code = 840 GROUP BY currency_code")
average_value = cursor.fetchone()[0]  # fetchone() повертаодє кортеж, беремо перший елемент
print("Середя вартість USD:", average_value)

# AVERAGE EURO
cursor.execute("SELECT AVG(value), currency_code FROM currency_2 WHERE currency_2.currency_code = 978 GROUP BY currency_code")
average_value = cursor.fetchone()[0]  # fetchone() повертаодє кортеж, беремо перший елемент
print("Середя вартість EUR:", average_value)

# cursor.execute("SELECT date, value FROM currency_2 WHERE currency_code=840")
# euro_values = cursor.fetchall()
# print(euro_values)
#
# import turtle
#
# # Налаштування вікна
# screen = turtle.Screen()
# screen.title("Графік курсу USD")
# screen.setup(width=600, height=400)
#
# # Налаштування черепашки
# pen = turtle.Turtle()
# pen.penup()
#
# min_val = cursor.execute("SELECT date, MIN(value) FROM currency_2 WHERE currency_code=840").fetchone()[1]
# print(min_val)
# max_val = cursor.execute("SELECT date, MAX(value) FROM currency_2 WHERE currency_code=840").fetchone()[1]
# print(max_val)
# y_range = max_val - min_val
#
# # # Висота графіку у пікселях
# graph_height = 300
# #
# # # Масштаб: скільки пікселів на 1 одиницю значення
# scale_y = graph_height / y_range
# graph_width = 500
# scale_x = graph_width / (len(euro_values) - 1)
# x = -graph_width/2
#
#
# first_y = (euro_values[0][1] - min_val) * scale_y
# pen.goto(-graph_width/2, first_y)  # початкова X= -graph_width/2
# pen.pendown()  # від цього моменту починаємо малювати
#
# for item in euro_values[1:]:
#     y = (item[1] - min_val) * scale_y
#     print(y)
#     pen.goto(x,  y )
#     pen.dot(3, "black")
#     x += scale_x
# turtle.done()