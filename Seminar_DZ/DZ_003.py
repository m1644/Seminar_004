'''
3. Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_value(list):
    return [i for i in set(list)]

size = int(input('Задайте кол-во чисел в списке: '))
m = int(input('Задайте начальное значение в списке: '))
n = int(input('Задайте конечное значение в списке: '))

origin = create_list(size, m, n)
print(f'Исходный список {origin}')
print(f'Список неповторяющихся элементов {get_value(origin)}')
