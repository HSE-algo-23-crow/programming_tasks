import time


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if type(n) != int:
        raise Exception('Параметр n не является целом числом')
    if n < 1:
        raise Exception('Параметр n меньше 1')

    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if type(n) != int:
        raise Exception('Параметр n не является целым числом')
    if n < 1:
        raise Exception('Параметр n меньше 1')

    fib1 = fib2 = 1
    n -= 3

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return fib2


def rabbits(month: int, lifetime: int) -> int:
    """Возвращает количество пар кроликов в популяции на заданный месяц.
    В начальный момент времени имеется одна пара кроликов. Начиная со второго
    месяца после рождения кролики производят новую пару кроликов каждый месяц.
    После достижения предельного возраста кролики умирают.

    :param month: количество месяцев жизни популяции
    :param lifetime: продолжительность жизни кролика, не менее 2 месяцев
    :return: количество пар кроликов
    """
    if month <= 0:
        raise Exception("Кол-во месяцев должно быть больше или равно единицы")
    elif month == 1:
        return 1
    else:
        pairs = [1, 1]
        for i in range(2, month):
            new_pairs = pairs[i-1] + pairs[i-2]
            if i >= lifetime:
                new_pairs -= pairs[i-lifetime]
            pairs.append(new_pairs)
        return pairs[-1]


def main():
    n = 35
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
