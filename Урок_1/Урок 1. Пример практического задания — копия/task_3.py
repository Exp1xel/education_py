"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""


n = input("Введите число n: ")
res = int(n) + int(n * 2) + int(n * 3)
print(f'{n} + {n * 2} + {n * 3} = {res}')

