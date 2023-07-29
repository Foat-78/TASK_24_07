# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import os
os.system('cls')

# # Первый вариант
# n = int(input("Введите общее кол-во чисел для первого множества n: "))
# m = int(input("Введите общее кол-во чисел для второго множества m: "))
# sp_n = []
# sp_m = []
# for _ in range(n):
#     sp_n.append(int(input("Введите элементы множества n: ")))
# for _ in range(m):
#     sp_m.append(int(input("Введите элементы множества m: ")))

# print(n, m)
# print(*sp_n)    
# print(*sp_m)
# new_numbers = []
# count = 0
# for i in sp_n:
#     for j in sp_m:   
#         if i == j:
#             count +=1
#             new_numbers.append(i)
# if count > 0:           
#     print(*sorted(set(new_numbers)))
# else:    
#     print(f"Повторяющиеся числа в множествах отсутствует!!!")

# Второй вариант
n = int(input("Введите общее кол-во элементов первого множества n: "))
m = int(input("Введите общее кол-во элементов второго множества m: "))
sp_n = []
sp_m = []
for _ in range(n):
    sp_n.append(int(input("Введите элементы множества n: ")))
for _ in range(m):
    sp_m.append(int(input("Введите элементы множества m: ")))

sp_n1 = set(sp_n)
sp_m1 = set(sp_m)
users3 = sp_n1.intersection(sp_m1)
print(n, m)
print(*sp_n)    
print(*sp_m)
print(*sorted(users3))

