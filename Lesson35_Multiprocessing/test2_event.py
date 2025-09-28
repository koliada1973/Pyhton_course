import multiprocessing
import time
import os
import random


def worker(event, process_id):
    """
    Робітник, який чекає на стартовий сигнал.
    """
    pid = os.getpid()

    print(f"[{process_id}] Процес {pid} готовий і чекає старту...")

    # 1. Очікування: Процес блокується тут
    event.wait()

    # 2. Робота після сигналу
    print(f"[{process_id}] >>> СТАРТ! Процес {pid} починає роботу.")

    # Імітація роботи
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)

    print(f"[{process_id}] Процес {pid} завершив роботу за {delay:.2f} с.")


if __name__ == '__main__':
    # 1. Створення об'єкта Події
    start_event = multiprocessing.Event()

    num_workers = 3
    processes = []

    # Створення та запуск дочірніх процесів
    for i in range(num_workers):
        p = multiprocessing.Process(target=worker, args=(start_event, i + 1))
        processes.append(p)
        p.start()

    print("\n--- Батьківський процес чекає, поки всі дочірні процеси запустяться ---\n")
    # Короткий сон, щоб дати час усім робітникам запуститися і викликати event.wait()
    time.sleep(1)

    print("Батьківський процес надсилає стартовий сигнал через 3 секунди...")
    time.sleep(3)

    # 3. Надсилання сигналу: Встановлюємо прапорець у True
    print("\n*** SET: Надсилаємо сигнал Event! ***\n")
    start_event.set()

    # 4. Очікування завершення всіх процесів (join())
    for p in processes:
        p.join()

    print("\n--- Всі процеси завершили роботу. Програма завершена. ---")