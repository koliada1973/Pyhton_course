# Доопрацюйте задачу 3 наступним чином.
# Додайте ще один потік, зробіть його демоном-логером,
# організуйте вивід логів в зовнішній файл (з частотою 100 раз в секунду) в форматі: ім’я потоку, дата, час.
# При виході з головного потоку запринтіть дату та час. Порівняйте зі значенням дата:час в файлі логу.

import random
import threading
import datetime
import time
from datetime import datetime



def func_daemon(name):
    print(f'Thread {name} start')
    while True:
        with open('log.txt', 'a') as f:
            date_now = datetime.now()
            date_now = date_now.strftime('%Y-%m-%d, %H:%M:%S.%f')[:-3]
            result = f"{name} {date_now}\n"
            f.write(result)
            time.sleep(0.01)


def func(name):
    print(f'Thread {name} start')
    time.sleep(1)
    # x = random.randint(0, 100) ** random.randint(0, 100)
    print(f'Thread {name} end')


t1 = threading.Thread(target=func, args=(1,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func_daemon, args=(3,), daemon=True)



t1.start()
t2.start()
t3.start()
t1.join()
t2.join()


date_now = datetime.now()
date_now = date_now.strftime('%Y-%m-%d, %H:%M:%S.%f')[:-3]
print(date_now)