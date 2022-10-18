# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Mulptiple_Couple():
    for i in range(n):
        list_Multiple_Couple.append(list_Numbers[i] * list_Numbers[len(list_Numbers) - 1 - i])
    return list_Multiple_Couple


try:
    list_Numbers = [20, 30, 40, 50, 60]
    list_Multiple_Couple = []

    n = len(list_Numbers)/2
    if n%2 != 0:
        n += 0.5
        n = int(n)
    Mulptiple_Couple()    
    print(list_Multiple_Couple)

except:
    print('xrusha')
