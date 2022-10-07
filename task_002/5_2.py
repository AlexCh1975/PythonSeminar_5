from doctest import OutputChecker


# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую
# последовательность. Порядок элементов менять нельзя.

# in 8
# Out
# >>> [10, 0, 5, 11, 6, 1, 15, 10]
# >>> [[10,11,15], [0,5,6,15], [5, 11,15], [11,15], [6,15], [1,15]]

# in 10
# Out
# >>> [19, 5, 1, 14, 5, 9, 15, 11, 12, 2]
# [[5,14,15], [1, 14, 15], [14,15], [5,9,15], [9,15], [11,12]]

import random

def create_list(size: int):
    size = size if size > 0 else -size

    return random.choices(range(size * 2), k = size)

def creating_list_lists(nums: list):
    numbers = []

    for i in range(len(nums)):
        some = nums[i]
        temp = [some]
        for j in range(i + 1, len(nums)):
            if nums[j] > some:
                temp.append(nums[j])
                some = nums[j]
        if len(temp) > 1:
            numbers.append(temp)

    return numbers

nums = create_list(int(input("Число: ")))
print(nums)
print(creating_list_lists(nums))