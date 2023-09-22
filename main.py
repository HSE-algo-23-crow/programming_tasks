import time


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    # Проверки на ввод данных
    if type(n) != int:
        raise Exception('Введённое значение n не является типом int')
    elif n < 1:
        raise Exception('Введённое значение n не может быть меньше единицы')

    # Решение
    if n < 3:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    # Проверки на ввод данных
    if type(n) != int:
        raise Exception('Введённое значение n не является типом int')
    elif n < 1:
        raise Exception('Введённое значение n не может быть меньше единицы')

    # Решение
    first = 1
    second = 1
    for _ in range(3, n+1):
        first, second = second, first+second
    return second

def rabbits(month: int, lifetime: int) -> int:
    """Возвращает количество пар кроликов в популяции на заданный месяц.
    В начальный момент времени имеется одна пара кроликов. Начиная со второго
    месяца после рождения кролики производят новую пару кроликов каждый месяц.
    После достижения предельного возраста кролики умирают.

    :param month: количество месяцев жизни популяции
    :param lifetime: продолжительность жизни кролика, не менее 2 месяцев
    :return: количество пар кроликов
    """
    # Проверки на ввод данных
    if type(month) != int or type(lifetime) != int:
        raise Exception('одно из введённых значений не является типом int')
    elif month < 1:
        raise Exception('Введённое значение month не может быть меньше единицы')
    elif lifetime < 2:
        raise Exception('Введённое значение lifetime не может быть меньше двух')

    # Решение
    if month < 3:
        return 1

    if lifetime < month:
        return rabbits(month-1, lifetime) + rabbits(month-2, lifetime)-rabbits(month-lifetime, lifetime)
    else:
        return rabbits(month-1, lifetime)+rabbits(month-2, lifetime)


def main():
    n = 25
    print(f'Вычисление {n} числа Фибоначчи рекурсивно:')
    start_time = time.time()
    print(fibonacci_rec(n))
    print(f'duration: {time.time() - start_time} seconds')

    print(f'\nВычисление {n} числа Фибоначчи итеративно:')
    start_time = time.time()
    print(fibonacci_iter(n))
    print(f'duration: {time.time() - start_time} seconds')

    lifetime = 6
    month = 5
    print(f'\nВычисление числа пар кроликов по состоянию на {month} месяц')
    print(f'при продолжительности жизни кролика {lifetime} месяцев')
    print(rabbits(month, lifetime))


if __name__ == '__main__':
    main()