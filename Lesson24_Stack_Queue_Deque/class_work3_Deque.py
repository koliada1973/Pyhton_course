# . Реалізувати структуру двостороння черга з (через створення класу, з допомогою list) методами:
# add_front
# add_rear
# remove_front
# remove_rear
# is_empty
# size
# __str__ (вивести список елементів: індекс, значення)

import random
List_10000 = [random.randint(-10000, 10000) for i in range(10000)]
List_50000 = [random.randint(-10000, 10000) for i in range(50000)]
List_100000 = [random.randint(-10000, 10000) for i in range(100000)]

import time
class My_Deque:
    def __init__(self):
        self.my_deque = []

    def add_front(self, data):
        self.my_deque.insert(0, data)

    def add_rear(self, data):
        self.my_deque.append(data)

    def remove_front(self):
        return self.my_deque.pop(0)

    def remove_rear(self):
        return self.my_deque.pop()

    def is_empty(self):
        return self.my_deque == []

    def size(self):
        return len(self.my_deque)

    def __str__(self):
        return [(i, d) for i, d in enumerate(self.my_deque)]

q = My_Deque()
start = time.time()
for i in List_10000:
    q.add_front(i)
finish = time.time()
delta_t = finish - start
print(f"час додавання add_front (10000) = {delta_t:.5f} сек.")

start = time.time()
q.add_front('i')
finish = time.time()
delta_t = finish - start
print(f"час додавання add_front (1) = {delta_t} сек.")

start = time.time()
q.remove_rear()
finish = time.time()
delta_t = finish - start
print(f"час видалення remove_rear (1) = {delta_t} сек.")

print()
start = time.time()
for i in List_10000:
    q.add_rear(i)
finish = time.time()
delta_t = finish - start
print(f"час додавання add_rear (10000) = {delta_t:.5f} сек.")

start = time.time()
q.add_rear('i')
finish = time.time()
delta_t = finish - start
print(f"час додавання add_rear (1) = {delta_t} сек.")

start = time.time()
q.remove_front()
finish = time.time()
delta_t = finish - start
print(f"час видалення remove_front (1) = {delta_t} сек.")