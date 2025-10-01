# Обчислення чисел Фібоначі (з допомогою рекурсії), які займають кілька секунд.
# Запустіть 3 рази для кількох обчислень, послідовно, та з використанням asyncio.
# Виміряйте час, для обох випадків.
# Також порівняйте час виконання з реалізацією за допомогою потоків та процесів.

import asyncio
import time

# Обчислення чисел Фібоначчі чисто CPU-bound (жодного I/O немає), тому asyncio не дасть реального прискорення —
# всі задачі по черзі будуть чекати результату.
# Для рекурсивних CPU-функцій у Python краще або залишити їх синхронними,
# або винести у asyncio.to_thread / multiprocessing.

# 1 Варіант - синхронний:
def fibonacci(n):
    """Функція розрахунку n-ного числа Фібоначчі (рекурсівна)"""
    if n <= 1:
        return n
    return  fibonacci(n - 1) +  fibonacci(n - 2)

def main():
    num_list = [34, 35, 36]
    result = []

    start_time2 = time.perf_counter()

    for i in num_list:
        result.append(fibonacci(i))

    duration2 = time.perf_counter() - start_time2
    print(result)
    print(f"Розрахунок чисел Фібоначчі (сінхронний метод) за {duration2} сек.")


# 2 Варіант - псевдоасинхронний (рекурсія синхронна, а виклики виконуються через asyncio.to_thread):
async def async_wrapper(func, n):
    """Функція, яка запускає синхронну функцію в окремому потоці."""
    return await asyncio.to_thread(func, n)

async def main2():
    num_list = [34, 35, 36]
    tasks = []

    start_time = time.perf_counter()

    for num in num_list:
        tasks.append(asyncio.create_task(async_wrapper(fibonacci, num)))
    results = await asyncio.gather(*tasks)

    duration = time.perf_counter() - start_time
    print(results)
    print(f"Розрахунок чисел Фібоначчі (псевдоасінхронний метод) за {duration} сек.")



# 3 Варіант - асинхронний (чисто асинхронна рекурсія (але це повільніше):
async def fibonacci3(n: int) -> int:
    if n <= 1:
        return n
    return await fibonacci3(n - 1) + await fibonacci3(n - 2)

async def main3():
    num_list = [34, 35, 36]
    result = []

    start_time3 = time.perf_counter()

    tasks = [fibonacci3(i) for i in num_list]
    result = await asyncio.gather(*tasks)

    duration3 = time.perf_counter() - start_time3
    print(result)
    print(f"Розрахунок чисел Фібоначчі (повністю асінхронний метод) за {duration3} сек.")



# 4 Варіант - мультипроцессінг
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor

def main4():
    num_list = [34, 35, 36]

    start_time4 = time.perf_counter()

    # Більш застарілий метод:
    # with Pool() as pool:
    #     result = pool.map(fibonacci, num_list)

    # Сучасніший та більш зручний метод:
    with ProcessPoolExecutor() as executor:
        result = list(executor.map(fibonacci, num_list))

    duration4 = time.perf_counter() - start_time4
    print(result)
    print(f"Розрахунок чисел Фібоначчі (мультипроцессорний метод) за {duration4} сек.")



# 5 Варіант - мультитредінг
from concurrent.futures import ThreadPoolExecutor

def main5():
    num_list = [34, 35, 36]

    start_time5 = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        result = list(executor.map(fibonacci, num_list))

    duration5 = time.perf_counter() - start_time5
    print(result)
    print(f"Розрахунок чисел Фібоначчі (мультитрединговий метод) за {duration5} сек.")

if __name__ == '__main__':
    main()                      # Сінхронний метод                          14.396432699999423 сек.
    asyncio.run(main2())        # рекурсія синхронна (псевдоасинхронність)  14.377225399999588 сек.
    asyncio.run(main3())        # чисто асинхронна рекурсія (але це довше)  28.58985869999742 сек.
    main4()                     # мультипроцессінг                          7.259921700002451 сек.
    main5()                     # мультитредінг                             14.373179000001983 сек.