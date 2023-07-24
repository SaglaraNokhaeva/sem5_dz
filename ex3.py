# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

count = int(input('Введите длину ряда Фибоначчи: '))

def fib(n):
    if n == 1:
        print('1')
    elif n == 2:
        print('1 1', end=' ')
    else:
        f1 = f2 = 1
        print('1 1', end=' ')
        for i in range(2, n):
            f1, f2 = f2, f1 + f2
            yield f2

print(*fib(count))
