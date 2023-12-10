"""
Задание 2.

Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

my_lst = input("Введите целые числа через пробел: ").split(' ')
i, j = 0, 1
while len(my_lst) > j:
    my_lst[i], my_lst[j] = my_lst[j], my_lst[i]
    i += 2
    j += 2

# Строка print(*my_lst) передаёт все элементы списка my_lst в вызов print()
# как отдельные аргументы
print('Результат:', *my_lst)
