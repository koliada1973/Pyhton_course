# task 1, 2
# bubble method

import copy
import random
import time

def func_min_bubble(my_list):
    my_list_1 = copy.deepcopy(my_list)

    # print(my_list_1)

    for j in range(len(my_list_1) - 1):
        for i in range(len(my_list_1) - 1):
            if my_list_1[i] > my_list_1[i+1]:
                my_list_1[i], my_list_1[i + 1] = my_list_1[i+1], my_list_1[i]

        # print(my_list_1)
        # print(j, '****************')
    # print(id(my_list), id(my_list_1))


def func_min_min(my_list):
    my_list_1 = copy.deepcopy(my_list)
    my_min = my_list_1[0]
    for i in range(len(my_list_1)):
        if my_min >  my_list_1[i]:
            my_min = my_list_1[i]
    # print(my_min)


my_list_10 = [random.randint(0,2000) for i in range(10000)]
# my_list_10_1 = [random.randint(0,2000) for i in range(10000)]
# my_list_10_2 = [random.randint(0,2000) for i in range(10000)]

time_start = time.time()
func_min_bubble(my_list_10)
print(f'func_min_bubble finished in {time.time() - time_start} s, with my_list_10')
print(my_list_10)

time_start = time.time()
func_min_min(my_list_10)
print(f'func_min_min finished in {time.time() - time_start} s, with my_list_10')
print(my_list_10)

time_start = time.time()
my_list_10.sort()
print(f' .sort() finished in {time.time() - time_start} s, with my_list_10')
print(my_list_10)