import time

list1 = list(range(1_000_000))
set1 = set(list1)

el = 999_999

# Перевірка в списку
t1 = time.time()
print(el in list1)
print("Список:", time.time() - t1, "сек")

# Перевірка в множині
t2 = time.time()
print(el in set1)
print("Множина:", time.time() - t2, "сек")