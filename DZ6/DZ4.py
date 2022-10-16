# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

n = int(input('Введите размер списка '))
list1 = [round(uniform(0,9),2) for i in range(n)]

min = min(list1, key=lambda i: float(i))
max = max(list1, key=lambda i: float(i))

dif = (max - int(max)) - (min - int(min))

print(list1)
print(max, min)
print(round(dif,2))

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# new_lst = [round(i%1,2) for i in lst]
# print(lst, '=>', max(new_lst) - min(new_lst)) - Вариант проще