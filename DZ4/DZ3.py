# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

N = int(input('Введите число: '))
list = []
for i in range(1,N+1):
    a = randint(-N,N+1)
    list.append(a)
print(list)

newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)


a = [1,2,2,2,2,3,1,4]

print(set(a))

# from random import randint

# def create_list(size, m, n):
#     return [randint(m, n) for i in range(size)]

# def get_unic_value(list):
#     return [i for i in set(list)]

# size = 10
# m = 1
# n = 10

# origin = create_list(size, m, n)
# print(origin)
# print(get_unic_value(origin))