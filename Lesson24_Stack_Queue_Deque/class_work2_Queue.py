# Задачі:
# Увага! Для задач згенерувати 3 списки цілих випадкових чисел розміром 10000, 50000, 100000 елементів.
# Ці списки будуть використовуватись в кожній з задач.
#
# Для кожної задачі перевірити швидкодію кожного з методів,
# заміряючи час виконання (якщо час виконання = 0 секунд,
# збільшіть розмір списку або точність вимірювань (мілі- або мікро-секунди)),
# і зробити висновок про складність алгоритму методу в нотації Big O.
# 2. Реалізувати структуру черга (через створення класу, з допомогою list) з методами:
# enqueue
# dequeue
# is_empty
# size
# __str__ (вивести список елементів: індекс, значення)

import random
import time

List_10000 = [random.randint(-10000, 10000) for i in range(10000)]
List_50000 = [random.randint(-10000, 10000) for i in range(50000)]
List_100000 = [random.randint(-10000, 10000) for i in range(100000)]

class MyQueue:
    def __init__(self):
        self.my_queue = []

    def unqueue(self, data):
        self.my_queue.insert(0,data)

    def dequeue(self):
        self.my_queue.pop()

    def is_empty(self):
        return len(self.my_queue) == 0

    def size(self):
        return len(self.my_queue)

    def __str__(self):
        return [(i, d) for i, d in enumerate(self.my_queue)]

# q = MyQueue()
# start = time.time()
# for i in List_10000:
#     q.unqueue(i)
# finish = time.time()
# delta_t = finish - start
# print(f"час додавання (10000) = {delta_t:.5f} сек.")
#
# start = time.time()
# q.unqueue('i')
# finish = time.time()
# delta_t = finish - start
# print(f"час додавання (1) = {delta_t} сек.")
#
# start = time.time()
# q.dequeue()
# finish = time.time()
# delta_t = finish - start
# print(f"час видалення (1) = {delta_t} сек.")

# print(q.__str__())