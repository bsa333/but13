#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls' if os.name == 'nt' else 'clear')

num = int(input("Введите число: "))
i = 2 
lst = []
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
    else:
        i += 1
print(f"Простые множители: {lst}")
