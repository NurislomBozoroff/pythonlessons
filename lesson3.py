# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import uniform
x = [2, 3, 6, 10, 12, 16, 5]
# print(x)
summ = 0
for i in range(1, len(x), 2):
    # if i % 2 == 1:
    summ += x[i]
print(f"{x} -> сумма элементов на нечётных позициях: {summ}")


#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#    [2, 3, 4, 5, 6] = > [12, 15, 16];
#	[2, 3, 5, 6] = > [12, 15].



def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)


lst = [2, 3, 4, 5, 6]
mult_lst(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


n = int(input('Введите размер списка '))
list1 = []
for i in range(n):
    f = uniform(0, 9)
    list1.append(round(f, 2))

min = list1[0]
max = 0
for i in range(len(list1)):

    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))

print(list1)
print(max, min)
print(round(dif, 2))


#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#    45 -> 101101;
#    3 -> 11;
#    2 -> 10.


s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))

while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)


#Задача: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)
