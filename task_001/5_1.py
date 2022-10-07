# В файле находится N натуральных чисел, записанных через пробел. Среди чисел
# не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти это число. 

#  in 10 
#  out [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
#  9

#  in 10
#  out [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# -1

import random

def get_arr():
    path = 'task_001/input.txt'
    with open(path, 'r', encoding='utf_8') as data:
        arr = list(map(int, (data.readline().split(' '))))
    arr.remove(random.choice(arr))
    print(arr)
    return arr

def check_arr(arr):
    if arr[0] != 0:
        return 0
 
    for i in range(1, len(arr)):
        if (arr[i] - 1) != arr[i - 1]:
            return arr[i] -1
    return -1

num = check_arr(get_arr())
print(num)