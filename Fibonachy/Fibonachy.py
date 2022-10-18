# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
    # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
    
def fibanachi(n):
    if n in (1, 2): 
        return 1
    else: 
        return fibanachi(n-1) + fibanachi(n-2)

N = int(input('Enter n: '))
fib_arr = []

for i in range(1, N + 1):
    fib_arr.append(fibanachi(i))
fib_arr.insert(0, 0)

for i in range(1, N + 1):
    fib_arr.insert(0, ((-1)**(i + 1)) * fibanachi(i))
print(fib_arr)
