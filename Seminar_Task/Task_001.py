'''
1. Задайте строку из набора чисел. Напишите программу, 
которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
'''

list = []
s = '1 15 16 4 24 8 44 7'
list = s.split()
print(list)

max = int(list[0])
min = int(list[0])
for i in range(len(list)):
    if int(list[i]) > max:
        max = int(list[i])
    elif int(list[i]) < min:
        min = int(list[i])
print(f'Максимальное число = {max}, минимальное = {min}')
