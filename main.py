import time


def gcd_recursive(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух целых чисел.
    Рекурсивная реализация

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    :return: значение наибольшего общего делителя
    """
    validate_value_gcd(a, b)

    a = abs(a)
    b = abs(b)

    if a*b == 0:
        return a+b
    return gcd_recursive(max(a, b)-min(a, b), min(a, b))


def gcd_iterative_slow(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух целых чисел.
    Медленная итеративная реализация

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    :return: значение наибольшего общего делителя
    """
    validate_value_gcd(a, b)
    a, b = abs(a), abs(b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def gcd_iterative_fast(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух целых чисел.
    Быстрая итеративная реализация

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    :return: значение наибольшего общего делителя
    """
    validate_value_gcd(a, b)
    a, b = abs(a), abs(b)
    temp: int
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(a: int, b: int) -> int:
    """Вычисляет наименьшее общее кратное двух натуральных чисел

    :param a: натуральное число a
    :param b: натуральное число b
    :raise Exception: если a или b не являются натуральными числами или
    они равны нулю
    :return: значение наименьшего общего кратного
    """
    validate_value_lcm(a, b)
    a, b = abs(a), abs(b)
    return a*b // gcd_iterative_fast(a, b)


def validate_value_gcd(a, b):
    if type(a) != int:
        raise TypeError('Значение параметра a не является целым числом')
    if type(b) != int:
        raise TypeError('Значение параметра b не является целым числом')
    if a == 0 and b == 0:
        raise ValueError('Значения параметров a и b равны нулю')


def validate_value_lcm(a, b):
    if type(a) != int or a < 1:
        raise ValueError('Значение параметра a не является натуральным положительным числом')
    if type(b) != int or b < 1:
        raise ValueError('Значение параметра b не является натуральным положительным числом')


def main():
    a = 30
    b = 24
    print(f'Вычисление НОД чисел {a} и {b} рекурсивно:')
    start_time = time.time()
    print(gcd_recursive(a, b))
    print(f'Продолжительность: {time.time() - start_time} сек')

    print(f'\nВычисление НОД чисел {a} и {b} итеративно с вычитанием:')
    start_time = time.time()
    print(gcd_iterative_slow(a, b))
    print(f'Продолжительность: {time.time() - start_time} сек')

    print(f'\nВычисление НОД чисел {a} и {b} итеративно с делением:')
    start_time = time.time()
    print(gcd_iterative_fast(a, b))
    print(f'Продолжительность: {time.time() - start_time} сек')

    print(f'\nВычисление НОК чисел {a} и {b}:')
    start_time = time.time()
    print(lcm(a, b))
    print(f'Продолжительность: {time.time() - start_time} сек')


if __name__ == '__main__':
    main()