import time
from functools import lru_cache

def validate_gcd_nums(a, b):
    if not isinstance(a, int):
        raise Exception("Значение параметра a не является целым числом")

    if not isinstance(b, int):
        raise Exception("Значение параметра b не является целым числом")

    if a == 0 and b == 0:
        raise Exception("Значения параметров a и b равны нулю")

def validate_lcm_nums(a, b):
    if not isinstance(a, int) or a < 1:
        raise Exception('Значение параметра a не является натуральным положительным числом')

    if not isinstance(b, int) or b < 1:
        raise Exception('Значение параметра b не является натуральным положительным числом')

@lru_cache
def gcd_recursive(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух целых чисел.
    Рекурсивная реализация

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    :return: значение наибольшего общего делителя
    """
    validate_gcd_nums(a, b)
    a, b = abs(a), abs(b)

    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd_iterative_slow(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух целых чисел.
    Медленная итеративная реализация

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    :return: значение наибольшего общего делителя
    """
    validate_gcd_nums(a, b)
    a, b = abs(a), abs(b)

    while a != b and a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
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
    validate_gcd_nums(a, b)
    a, b = abs(a), abs(b)

    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Вычисляет наименьшее общее кратное двух натуральных чисел

    :param a: натуральное число a
    :param b: натуральное число b
    :raise Exception: если a или b не являются натуральными числами или
    они равны нулю
    :return: значение наименьшего общего кратного
    """
    validate_lcm_nums(a, b)
    a, b = abs(a), abs(b)

    return a * b // gcd_iterative_fast(a, b)


def main():
    a = 1005002
    b = 1354
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
