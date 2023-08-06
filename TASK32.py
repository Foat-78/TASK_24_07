# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import os
os.system('cls')

def index_min_max(array, min, max):
    index_arr = []
    [index_arr.append(i) for i in range(len(array)) if array[i] >= min and array[i] <= max]
    return index_arr


arr = [1, 5, 88, 100, 2, -4]
index_min = 33
index_max = 200
# arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# index_min = 3
# index_max = 10
print(arr)
print(index_min_max(arr, index_min, index_max))