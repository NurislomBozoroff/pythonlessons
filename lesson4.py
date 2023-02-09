# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

import math

d = input('Введите степень округления в формате 0.01 от 10 в степени -1 до 10 в степени -10 -> ')
d = d[2:len(d)]
print(round(math.pi,len(d)))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2  # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")



# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов \
# исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")




# Задана натуральная степень k. Сформировать случайным образом список \
# коэффициентов (значения от 0 до 100) многочлена и записать в файл \
# многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.

import random


def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return  lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) -  1and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) -  2and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) -  1and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) -  1and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))





# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача сформировать файл, содержащий сумму многочленов.

from itertools  import*
from Task033 import get_polynomial
import os
os.system("cls")


file1 = 'task033_1.txt'
file2 = 'task033_2.txt'


def read_pol(file): # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(pol):  # удалили "хвостик" и порезали" строку на массив , разделитель знак " + "
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol


pol1 = read_pol(file1)
pol2 = read_pol(file2)
print('Исходные полиномы:')
print(pol1)
print(pol2)
print('_'*30)
print(convert_pol(pol1))
print(convert_pol(pol2))
pol1_coef = list(map(int, convert_pol(pol1)))
pol2_coef = list(map(int, convert_pol(pol2)))
print(pol1_coef)
print(pol2_coef)
print('_'*30)

sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
print(sum_coef)
sum_coef = sum_coef[::-1]
print(sum_coef)
sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
print('Итоговый результат сложения полиномов:\n', sum_pol)
with open('task034.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol)




