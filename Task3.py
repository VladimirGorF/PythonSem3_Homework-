
# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def fractional_Parts(Numbers):
    for i in range(len(Numbers)):
        Numbers[i] -= int(Numbers[i])
        Numbers[i] = round(Numbers[i], 2)


def range_to_Max(Numbers):
    for i in range(len(Numbers)):
        for i in range(len(Numbers) - 1 - i):
            if Numbers[i] > Numbers[i + 1]:
                Numbers[i], Numbers[i + 1] = Numbers[i + 1], Numbers[i]


def diff_fraction(Numbers):
    for i in range(len(Numbers)):
        if Numbers[i] > 0:
            return (Numbers[len(Numbers) - 1] - Numbers[i])


try:
    Numbers = [1.1, 1.2, 3.1, 5, 10.01]

    fractional_Parts(Numbers)
    range_to_Max(Numbers)
    print(diff_fraction(Numbers))
except:
    print('Somthing is wrong!')
