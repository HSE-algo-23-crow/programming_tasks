import time


def gcd_recursive(a: int, b: int) -> int:
    if a is None:
        raise Exception("Значение параметра a не является целым числом")
    if b is None:
        raise Exception("Значение параметра b не является целым числом")
    if not isinstance(a, int):
        raise Exception("Значение параметра a не является целым числом")
    if not isinstance(b, int):
        raise Exception("Значение параметра b не является целым числом")
    a, b = abs(a), abs(b)  # Преобразовываем числа в положительные значения
    if a == 0 and b == 0:
        raise Exception("Значения параметров a и b равны нулю")
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd_iterative_slow(a: int, b: int) -> int:
    if a is None:
        raise Exception("Значение параметра a не является целым числом")
    if b is None:
        raise Exception("Значение параметра b не является целым числом")
    if not isinstance(a, int):
        raise Exception("Значение параметра a не является целым числом")
    if not isinstance(b, int):
        raise Exception("Значение параметра b не является целым числом")
    a, b = abs(a), abs(b)  # Преобразовываем числа в положительные значения
    if a == 0 and b == 0:
        raise Exception("Значения параметров a и b равны нулю")
    while b != 0:
        a, b = b, a % b
    return a


def gcd_iterative_fast(a: int, b: int) -> int:
    if a is None:
        raise Exception("Значение параметра a не является целым числом")
    if b is None:
        raise Exception("Значение параметра b не является целым числом")
    if not isinstance(a, int):
        raise Exception("Значение параметра a не является целым числом")
    if not isinstance(b, int):
        raise Exception("Значение параметра b не является целым числом")
    a, b = abs(a), abs(b)  # Преобразовываем числа в положительные значения
    if a == 0 and b == 0:
        raise Exception("Значения параметров a и b равны нулю")
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise Exception("Значение параметра a не является натуральным положительным числом")
    if not isinstance(b, int):
        raise Exception("Значение параметра b не является натуральным положительным числом")
    if a < 1:
        raise Exception("Значение параметра a не является натуральным положительным числом")
    if b < 1:
        raise Exception("Значение параметра b не является натуральным положительным числом")
    a, b = abs(a), abs(b)  # Преобразовываем числа в положительные значения
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
