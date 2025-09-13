from sort_algoritms import *
from Task1_v1 import bubbleSort_plus


# def insertion_sort(arr):
#     for i in range(len(arr)):
#         cursor = arr[i]
#         pos = i
#
#         while pos > 0 and arr[pos - 1] > cursor:
#             # Swap the number down the list
#             arr[pos] = arr[pos - 1]
#             pos = pos - 1
#         # Break and do the final swap
#         arr[pos] = cursor
#
#     return arr

# Використання
if __name__ == '__main__':
    import random

    l = [random.randint(-100, 100) for i in range(100)]
    print(f'Невідсортований список:     {l}')

    import time

    b1 = l.copy()
    start = time.time()
    b1 = bubbleSort_plus(b1)
    end = time.time()
    print(f'bubbleSort_plus ({(end - start):.6f}): {b1}')


    b = l.copy()
    start = time.time()
    bubble_sort(b)
    end = time.time()
    print(f'bubble_sort     ({(end - start):.6f}): {b}')

    s = l.copy()
    start = time.time()
    selection_sort(s)
    end = time.time()
    print(f'selection_sort  ({(end - start):.6f}): {s}')

    i = l.copy()
    start = time.time()
    insertion_sort(i)
    end = time.time()
    print(f'insertion_sort  ({(end - start):.6f}): {i}')