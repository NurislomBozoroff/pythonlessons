
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

day = int(input())
if (day > 5 and day < 8):
    print("да")
else:
    print("нет")



#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3


x = int(input())
y = int(input())

if (x > 0 and y > 0):
    print("1")
elif (x < 0 and y > 0):
    print("2")
elif (x > 0 and y < 0):
    print("4")
elif (x < 0 and y < 0):
    print("3")



#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21


def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) * 2 + (b[1] - a[1]) * 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(
    f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")
