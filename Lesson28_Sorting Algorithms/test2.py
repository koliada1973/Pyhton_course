def bubbleSort(array):
    OK = True
    len_array = len(array)
    while OK:
        OK = False
        for i in range(len_array - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                OK = True
    return array

# Використання
if __name__ == '__main__':
    import random

    l = [random.randint(-100, 100) for i in range(100)]
    print(f'Невідсортований список:     {l}')

    import time

    b1 = l.copy()
    start = time.time()
    b1 = bubbleSort(b1)
    end = time.time()
    print(f'bubbleSort ({(end - start):.6f}): {b1}')