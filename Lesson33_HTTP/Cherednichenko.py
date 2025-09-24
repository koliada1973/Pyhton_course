import sqlite3
import requests
from datetime import datetime


def create_database():
    conn = sqlite3.connect('class33.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS currencies
                   (
                       code
                       INTEGER
                   (
                       3
                   ) PRIMARY KEY,
                       currency VARCHAR
                   (
                       20
                   ) NOT NULL
                       )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS exchange_rates
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       date
                       DATE
                       NOT
                       NULL,
                       value
                       REAL
                       NOT
                       NULL,
                       currency_code
                       INTEGER
                   (
                       3
                   ),
                       FOREIGN KEY
                   (
                       currency_code
                   ) REFERENCES currencies
                   (
                       code
                   )
                       )
                   ''')

    return conn, cursor


def fetch_nbu_data(val_code,date =None):
    """Отримання даних з API НБУ"""
    base_url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250101&end=20250919&valcode={val_code}&sort=exchangedate&order=desc&json"

    # if date:
    #     url = f"{base_url}?date={date}&json"
    # else:
    #     url = f"{base_url}?json"

    response = requests.get(base_url)
    return response.json()


def update_currency_data(conn, cursor,val_code):
    """Оновлення даних про валюти"""
    data = fetch_nbu_data(val_code)

    currencies_to_insert = []
    for item in data:
        currencies_to_insert.append((item['r030'], item['txt']))

    cursor.executemany('INSERT OR IGNORE INTO currencies VALUES (?, ?)', currencies_to_insert)
    conn.commit()


def update_exchange_rates(conn, cursor,val_code):
    """Оновлення курсів валют"""
    data = fetch_nbu_data(val_code)

    # current_date = date or datetime.now().strftime('%Y%m%d')

    # formatted_date = f"{current_date[:4]}-{current_date[4:6]}-{current_date[6:]}"

    rates_to_insert = []
    for item in data:
        rates_to_insert.append((item['exchangedate'], item['rate'], item['r030']))

    cursor.executemany('INSERT INTO exchange_rates (date, value, currency_code) VALUES (?, ?, ?)', rates_to_insert)
    conn.commit()


# Використання:
if __name__ == "__main__":
    conn, cursor = create_database()

    # Оновлюємо дані про валюти'
    update_currency_data(conn, cursor,val_code='eur')
    update_currency_data(conn, cursor, val_code='usd')
    update_currency_data(conn, cursor, val_code='gbp')

    # Оновлюємо курси за поточну дату
    update_exchange_rates(conn, cursor,val_code ='eur')
    update_exchange_rates(conn, cursor,val_code ='usd')
    update_exchange_rates(conn, cursor,val_code ='gbp')

    # Можна також отримати дані за конкретну дату
    # update_exchange_rates(conn, cursor, "20240115")

    conn.close()