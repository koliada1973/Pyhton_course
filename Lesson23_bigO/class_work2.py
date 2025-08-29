# Задача 2.
#  Відсортуйте список з допомогою методу "бульбашки".
#  Заміряйте час на виконання задачі, на масивах випадкових значень:
#  10 елементів в масиві
#  100
#  1000
#  Порівняйте результати з методом list.sort(), на тих самих масивах.

import random
import time

list1 = [random.randint(-10, 1000) for i in range(10)]
list2 = [random.randint(-10, 1000) for i in range(100)]
list3 = [random.randint(-10, 1000) for i in range(1000)]



# Сортировка бульбашкою
def bulbashka(list1):
    for i in range(len(list1)-1):
        for x in range(len(list1)-1):
            if list1[x] > list1[x+1]:
                list1[x], list1[x + 1] = list1[x + 1], list1[x]
    return list1

start = time.time()
bulbashka(list1)
end = time.time()
t1 = end - start
start = time.time()
list1.sort()
end = time.time()
t2 = end - start
print(f"10   елементів. Сортування бульбашкою: {t1:.10f} секунд, сортування list.sort(): {t2:.10f} секунд (швидше в {t1/t2:.0f} раз)")

start = time.time()
bulbashka(list1)
end = time.time()
t1 = end - start
start = time.time()
list1.sort()
end = time.time()
t2 = end - start
print(f"100  елементів. Сортування бульбашкою: {t1:.10f} секунд, сортування list.sort(): {t2:.10f} секунд (швидше в {t1/t2:.0f} раз)")

start = time.time()
bulbashka(list1)
end = time.time()
t1 = end - start
start = time.time()
list1.sort()
end = time.time()
t2 = end - start
print(f"1000 елементів. Сортування бульбашкою: {t1:.10f} секунд, сортування list.sort(): {t2:.10f} секунд (швидше в {t1/t2:.0f} раз)")