
# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_number(n):
    binar = []

    while n > 0:
        binar.insert(0, n % 2)
        n //= 2
    return binar

try:
    n = int(input('Please input an integer '))
    print(binary_number(n))
except:
    print('Please input an integers only!')


