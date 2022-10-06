# Напишите программу, которая найдёт произведение пар чисел списка (CСписок создаем как в предыдущем задании).
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list, ' => ' , list2)

# my_list = [2, 3, 4, 5, 6]
# result_list = []
# for i in range((len(my_list)+1)//2):
#     result_list.append(my_list[i]*my_list[len(my_list)-1-i])
# print(result_list)