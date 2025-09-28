# Task 2:
# Нам потрібно отримати 3 курса валют з API Нацбанку
# (припустимо що API за 1 раз повертає лише курс по одній валюті).
# Спробуємо це зробити синхронно (звичайний підхід), з використанням потоків і з використанням процесів.
# Виміряйте час, для всіх випадків (запустіть по 3 рази, для усереднення результату).

import requests
from datetime import date, timedelta
import json
import threading
import time
import multiprocessing


def NBU_request(start_date: date, end_date: date, val, list_data: list):
    """Функція, що надсилає запит на сайт НБУ, отримує курс валют за певний період часу -
     в нашому від попередньої доби до поточної доби і зберігає ці дані в форматі json в переданий список list_data
     (в запиті також вказується порядок сортування (зростання) за кодом валюти r030)"""

    # Рядок запиту:
    # https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20200302&json
    url = f"https://bank.gov.ua//NBUStatService/v1/statdirectory/exchange?valcode={val}&date={start_date}&json"

    response = requests.get(url)

    # Якщо дані отримано успішно - повертаємо дані у форматі json:
    if response.status_code == 200:
        json_response = response.json()
        list_data.append(json_response)
    else:
        print(f"Помилка {response.status_code} при отриманні даних з сайту")


def save_in_json_file(file_name: str, new_data):
    """Функція, що зберігає дані в файл json"""
    # Спочатку намагаємось прочитати наявні дані з файлу:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = []   # Якщо файлу не існує, або він пустий - створюємо новий список даних

    # Додаємо нові дані до списку
    data.append(new_data)

    # Записуємо оновлений список назад у файл
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Помилка при збереженні даних: [{e}]")



if __name__ == '__main__':
    # Потрібен список валют, по яких потрібно зробити запити:
    list_val = ['usd', 'eur', 'gbr']

    # дати:
    today = date.today().strftime("%Y%m%d")
    pre_date = date.today().strftime("%Y%m%d")


    # Для багатопотокового запиту потрібно створити
    # список для збереження результатів запитів,
    # та список thread для роботи з потоками:
    list_data = []
    list_threads = []

    # Варіант 1 - без створення потоків. Просто запити в циклі
    start_time2 = time.perf_counter()
    for val in list_val:
        NBU_request(pre_date, today, val, list_data)

    # Збереження всіх отриманих даних в файл:
    file_name = 'Exchang.json'
    for data in list_data:
            save_in_json_file(file_name, data)

    duration2 = time.perf_counter() - start_time2

    print(f"Отримання і збереження даних (без використання потоків) за {duration2} сек.")

    # Варіант 2 - з потоками.
    start_time1 = time.perf_counter()
    # Для запиту на сайт під кожну пару дат в списку list_dates створюємо свій потік.
    for val in list_val:
        t = threading.Thread(target=NBU_request, args=(pre_date, today, val, list_data))
        list_threads.append(t)
        t.start()

    # Очікуємо на завершення роботи всіх потоків:
    for t in list_threads:
        t.join()

    # Збереження всіх отриманих даних в файл:
    file_name = 'Exchang.json'
    for data in list_data:
            save_in_json_file(file_name, data)

    duration1 = time.perf_counter() - start_time1

    print(f"Отримання і збереження даних (з використанням потоків) за {duration1} сек.")


    # 3 Варіант. Мультіпроцессінг
    start_time1 = time.perf_counter()
    # Для запиту на сайт під кожну пару дат в списку list_dates створюємо свій потік.
    with multiprocessing.Pool() as pool:
        pool.apply_async(NBU_request, args=(pre_date, today, list_val))

    # Збереження всіх отриманих даних в файл:
    file_name = 'Exchang.json'
    for data in list_data:
        save_in_json_file(file_name, data)

    duration1 = time.perf_counter() - start_time1

    print(f"Отримання і збереження даних (з використанням процесів) за {duration1} сек.")



