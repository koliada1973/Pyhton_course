import random

num_list = [random.randint(0,10) for i in range(5)]
print(num_list)


for element in range(len(num_list)-1,0,-1):
    for passnum in range(len(num_list) - 1, 0, -1):
        for i in range(passnum):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

# for i in range(len(num_list)):
#     min = i
#     for j in range(i+1,len(num_list)):
#         if num_list[min] > num_list[j]:
#             min = j
#     num_list[i], num_list[min] = num_list[min], num_list[i]

print(num_list)