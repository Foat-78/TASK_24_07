# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

import os
os.system('cls')

N = int(input("Введите целое число N: "))
num = 1
while num <= N:
    print(num, end = " ")
    num *= 2