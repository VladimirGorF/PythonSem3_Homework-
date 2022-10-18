# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd(list_numbers):
    sum = 0
    for i in range(len(list_numbers)):
        if i%2 != 0:
            sum += list_numbers[i]
    return sum

try:
    list_numbers = [10, 20, 30, 40, 50]
    print(sum_odd(list_numbers))

except:
    print('хрюня')

