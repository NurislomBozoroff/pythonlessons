#Напишитe программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11

number = str(input('Введите число'))
summa = 0
i = 0
for i in number:
    summa += int(i)
    
print(summa)    

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)



def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")


#Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.

#Пример:

#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Enter number: '))


def sequence(n):

    return [round((1 + 1 / x)**x, 2) for x in range(1, n + 1)]


print(sequence(n))
print(round(sum(sequence(n))))


