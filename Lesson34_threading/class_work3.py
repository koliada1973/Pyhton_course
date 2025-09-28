# Реалізуйте функцію, яка виконує якесь обчислення,
# наприклад x = random.randint(0,100) ** random.randint(0,100),
# та виводить на print ім’я потоку та x .
# Створіть та запустіть функцію у 2-х потоках (задайте їм відповідні імена).

import random
import threading
import time

def func(name):
    print(f'Thread {name} start')
    time.sleep(0.1)
    x = random.randint(0, 100) ** random.randint(0, 100)
    print(f'Thread {name} end')

t1 = threading.Thread(target=func, args=(1,))
t2 = threading.Thread(target=func, args=(2,))

t1.start()
t2.start()
