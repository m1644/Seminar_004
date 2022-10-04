'''
3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
'''

x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))

def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(not ((greater % x == 0) and (greater % y == 0))):
        greater += 1
    else:
        return greater

if __name__ == "__main__":
    print(calculate_lcm(x, y))
