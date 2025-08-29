# Задача 1.
# Напишіть дві функції на мові Python для знаходження мінімального числа у списку.
# Перша функція повинна порівнювати кожне число з кожним іншим числом у списку O(n*n).
# Друга функція повинна бути лінійною O(n)

import random

list1 = [random.randint(-10, 1000) for i in range(1, 11)]
print(list1)

# Сортировка бульбашкою
def bulbashka(new_list):
    list1 = new_list.copy()
    for i in range(len(list1)-1):
        for x in range(len(list1)-1):
            if list1[x] > list1[x+1]:
                list1[x], list1[x + 1] = list1[x + 1], list1[x]
    return list1

print(f"Сортування бульбашкою: {bulbashka(list1)}")
print(f"min = {min(list1)}" )


# 2 Варіант
def min_sort(new_list):
    list1 = new_list.copy()
    my_min = list1[0]
    for i in range(1, len(list1)):
        if list1[i] < my_min:
            my_min = list1[i]
    return my_min

print(f"2 варіант сортування: {bulbashka(list1)}")
print(f"min = {min_sort(list1)}")