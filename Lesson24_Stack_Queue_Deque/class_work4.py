# 4. Виконати реалізацію структур, перелічених в задачах 2-3, з допомогою deque(from collections import deque).
# Згідно виконаних замірів часу виконання, який тип швидший ? list чи collections.deque

import random
import time

List_10000 = [random.randint(-10000, 10000) for i in range(10000)]
List_50000 = [random.randint(-10000, 10000) for i in range(50000)]
List_100000 = [random.randint(-10000, 10000) for i in range(100000)]

from collections import deque
q = deque()
start = time.time()
for i in List_10000:
    q.append(i)
finish = time.time()
delta_t = finish - start
print(f"час додавання append (10000) = {delta_t:.5f} сек.")

start = time.time()
q.append('i')
finish = time.time()
delta_t = finish - start
print(f"час додавання append (1) = {delta_t} сек.")

start = time.time()
q.pop()
finish = time.time()
delta_t = finish - start
print(f"час видалення pop (1) = {delta_t} сек.")