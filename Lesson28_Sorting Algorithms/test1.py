
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr

# Використання
if __name__ == '__main__':
    import random

    l = [random.randint(-100, 100) for i in range(100)]
    print(f'Невідсортований список:     {l}')

    import time

    b1 = l.copy()
    start = time.time()
    b1 = selection_sort(b1)
    end = time.time()
    print(f'bubbleSort_plus ({(end - start):.6f}): {b1}')