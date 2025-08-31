# Створіть клас Person, який ініціалізується лише ПІБ-ом (str, не мутабельний тип даних).
# Для порівняння екземплярів класу реалізуйте наступний алгоритм:
# спочатку порівнюються хеші від ПІБ. Якщо вони однакові, то можливо значення рівні і далі порівнюються самі значення.
# Якщо ж вони не однакові, то екземпляри вважаються не рівними.
# Порівняйте швидкодію такого підходу зі звичайним порівнянням (коли в методі __eq__ порівнюються лише значення ПІБ),
# створивши 2 списки (ПІБ потрібно згенерувати рандомний, довжина 10 літер) по 10 000 елементів з об’єктів класу.
import string


class Person:
    def __init__(self, PIB):
        self.PIB = PIB

    def __hash__(self):
        return hash(self.PIB)

    def __eq__(self, other):
        return self.PIB == other.PIB

    def __eq_hash__(self, other):
        if hash(self) == hash(other):
            return self.PIB == other.PIB
        else:
            return False


import random
def random_word(lenth=10):
    list1 = []
    return list1.append([random.choice(string.ascii_letters) for i in range(lenth)])
    # return [random.randint(0, 100000) for i in range(lenth)]

list_persons1 = [Person(random_word()) for i in range(1000)]
list_persons2 = [Person(random_word()) for i in range(1000)]

import time
start = time.time()
list3 = [list_persons1[i] for i in range(len(list_persons1)) if list_persons1 == list_persons2]
finish = time.time()
print(f"Delta time = {finish - start:0.6f} seconds")

start = time.time()
list3 = [list_persons1[i] for i in range(len(list_persons1)) if list_persons1[i].__eq_hash__ == list_persons2[i].__eq_hash__]
finish = time.time()
print(f"Delta time = {finish - start:0.6f} seconds")
