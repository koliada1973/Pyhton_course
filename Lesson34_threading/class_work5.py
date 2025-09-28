# Задача з навчального відео, про 2 000 000, без Lock().
# Виконайте та дослідіть, чому результат не збігся з тим,
# що був в навчальному відео (в відео результати не досягали 2 000 000,
# а у вас, мабуть всі рівні цьому значенню, особливо якщо версія python > 3.9).
# Також спробуйте запустити код з версією python <= 3.9
# (наприклад, в якомус он-лайн інтерпретаторі, наприклад www.online-python.com)

import threading

x = 0
def increment():
    global x
    x += 1

def thread_task():
    for _ in range(1000000):
        increment()

def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(x)

if __name__ == "__main__":
    main_task()

