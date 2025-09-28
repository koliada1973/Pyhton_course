# 2. (CPU-bound) Обчислення чисел Фібоначі (з допомогою рекурсії), які займають кілька секунд.
# Виконайте синхронно (але для різних чисел, наприклад 31, 32, 33
# щоб уникнути використання результатів з буферу), та з використанням процесів.
#  Виміряйте час, для обох випадків (запустіть по 3 рази, для усереднення результату) .
import multiprocessing
import time
import threading


def fibonacci(n):
    """Функція розрахунку n-ного числа Фібоначчі (рекурсівна)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    num_list = [34,35,36]
    result = []

    # 1 Варіант - синхронно
    start_time = time.perf_counter()
    for i in num_list:
        result.append(fibonacci(i))


    # for num in result:
    #     print(num)

    duration = time.perf_counter() - start_time
    print(f"Обчислення числа Фібоначчі (синхронний підхід :) за {duration} сек.")


    # 2 варіант - з використанням потоків
    list_threads = []
    start_time2 = time.perf_counter()

    for val in num_list:
        t = threading.Thread(target=fibonacci, args=(val,))
        list_threads.append(t)
        t.start()

    # Очікуємо на завершення роботи всіх потоків:
    for t in list_threads:
        t.join()

    # for num in result:
    #     print(num)

    duration2 = time.perf_counter() - start_time2
    print(f"Обчислення числа Фібоначчі (з використанням потоків) за {duration2} сек.")


    # 3 варіант - з використанням процесів
    start_time3 = time.perf_counter()

    # with multiprocessing.Pool() as pool:
    #     result = pool.map(fibonacci, num_list)

    proc_list = []
    for num in num_list:
        p = multiprocessing.Process(target=fibonacci, args=(num,))
        proc_list.append(p)
        p.start()

    for p in proc_list:
        p.join()
    # for num in result:
    #     print(num)

    duration3 = time.perf_counter() - start_time3
    print(f"Обчислення числа Фібоначчі (з використанням процесів) за {duration3} сек.")