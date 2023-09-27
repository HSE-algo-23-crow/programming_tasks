import time


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n in (1, 2):
        return 1
    return fibonacci_rec(n-1)+fibonacci_rec(n-2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    fib1 = fib2 = 1
    fib3 = 0
    for i in range(2,n):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    if n in (1, 2):
        return 1
    else:
        return fib3

def rabbits(month: int, lifetime: int) -> int:
    """Возвращает количество пар кроликов в популяции на заданный месяц.
    В начальный момент времени имеется одна пара кроликов. Начиная со второго
    месяца после рождения кролики производят новую пару кроликов каждый месяц.
    После достижения предельного возраста кролики умирают.

    :param month: количество месяцев жизни популяции
    :param lifetime: продолжительность жизни кролика, не менее 2 месяцев
    :return: количество пар кроликов
    """
    if month == 0:
        return 0
    elif month == 1:
        return 1
    else:
        rabbits = [1, 1]
        for i in range(2, month):
            if i < lifetime:
                rabbits.append(rabbits[i - 2] + rabbits[i - 1])
            elif i == lifetime or i == lifetime + 1:
                rabbits.append(rabbits[i - 2] + rabbits[i - 1] - 1)
            else:
                rabbits.append(rabbits[i - 2] + rabbits[i - 1] - rabbits[i - lifetime])
        return rabbits[-1]

def main():
    n = 20
    print(f'Вычисление {n} числа Фибоначчи рекурсивно:')
    start_time = time.time()
    print(fibonacci_rec(n))
    print(f'duration: {time.time() - start_time} seconds')

    print(f'\nВычисление {n} числа Фибоначчи итеративно:')
    start_time = time.time()
    print(fibonacci_iter(n))
    print(f'duration: {time.time() - start_time} seconds')

    if rabbits(1, 2):
        lifetime = 5
        print(f'\nВычисление числа пар кроликов по состоянию на {n} месяц')
        print(f'при продолжительности жизни кролика {lifetime} месяцев')
        print(rabbits(n, lifetime))


if __name__ == '__main__':
    main()
