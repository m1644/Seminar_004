'''
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
n = int(input('Введите натуральное число N: '))
list = []
for i in range(1, n + 1):
    if(n % i == 0):
      list.append(i)
print(f'Список множетелей числа {n} = {list}')
