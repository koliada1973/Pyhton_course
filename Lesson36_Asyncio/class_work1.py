from datetime import date
import json
import time
import asyncio
import aiohttp
import os


async def NBU_request(val):
    """Функція, що надсилає запит на сайт НБУ, отримує курс валют за певний період часу -
     в нашому випадку поточної доби і зберігає ці дані в форматі json в переданий список list_data,
     також зберігаємо дані в json-файл (це також I/O-bound операція)
     (в запиті також вказується порядок сортування (зростання) за кодом валюти r030)"""

    start_date = date.today().strftime("%Y%m%d")

    url = f"https://bank.gov.ua//NBUStatService/v1/statdirectory/exchange?valcode={val}&date={start_date}&json"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_response = await response.json()

                return json_response
            else:
                print(f"Помилка {response.status} при отриманні даних з сайту")




async def main():
    # Потрібен список валют, по яких потрібно зробити запити:
    list_val = ['usd', 'eur', 'gbp']

    # Список для зберігання результатів запитів
    results = []
    tasks = []

    start_time = time.perf_counter()

    for val in list_val:
        tasks.append(asyncio.create_task(NBU_request(val)))
    results = await asyncio.gather(*tasks)

    duration1 = time.perf_counter() - start_time

    print(results)
    print(f"Отримання і збереження даних (асінхронний метод) за {duration1} сек.")   # 0.10446699999738485 сек.


if __name__ == '__main__':
    asyncio.run(main())