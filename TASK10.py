"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
"""

import os
os.system('cls')


n = int(input("Введите количество монет на столе: "))
sp = []
for _ in range(n):
    sp.append(int(input("Введите 0 или 1 сторону монетки: ")))
num_one = 0
num_zeros = 0
for i in sp:
    if i == 0:
        num_zeros += 1
        coins = num_zeros
    else:
        num_one += 1
        coins1 = num_one
if coins < coins1:
    print(f'{n} - > {sp}')
    print(coins)
else:
    print(f'{n} - > {sp}')
    print(coins1)
