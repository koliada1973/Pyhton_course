# Повторіть задачу 6, застосувавши Lock(). Порівняйте час виконання задач 6 та 7.

import threading

lock = threading.Lock()
x = 0
def increment():
    global x
    x += 1

def thread_task():
    for _ in range(1000000):
        with lock:
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