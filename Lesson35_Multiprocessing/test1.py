from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    # запуск 4 робочих процесів
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print однакові числа у довільному порядку
        for i in pool.imap_unordered(f, range(10)):
            print(i, end=',')
        print()

        # асинхронно обчислити "f(20)"
        res = pool.apply_async(f, (20,))        # виконується *лише* в одному процесі
        print(res.get(timeout=1))                   # prints "400"

        # обчислити "os.getpid()" асинхронно
        res = pool.apply_async(os.getpid, ()) # виконується *лише* в одному процесі
        print(res.get(timeout=1))             # виводить PID цього процесу

        # запуск декількох оцінок асинхронно *може* використовувати більше процесів
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # змусити одного worker заснути на 10 секунд
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("Нам не вистачило терпіння і ми отримали помилку multiprocessing.TimeoutError")

        print("Наразі pool залишається доступним для подальшої роботи")

    # вихід з 'with'-блоку зупинив пул
    print("Зараз pool закритий і більше не доступний")