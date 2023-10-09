import time


def gcd_recursive(a: int, b: int) -> int:
    """Функция-обертка включает в себя проверку чисел на выполнение необходимых условий и вызов функции-вычислителя

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    :return: значение наибольшего общего делителя (через функцию-вычислитель)
    """
    gcd_validate(a, b)
    a = abs(a)
    b = abs(b)

    return gcd_recursive_computation(a, b)


def gcd_recursive_computation(a: int, b: int) -> int:
    """Функция-вычислитель - вычисляет наибольший общий делитель двух целых чисел.
        Рекурсивная реализация

        :param a: целое число a (a не равно 0)
        :param b: целое число b (b не равно 0)
        :return: значение наибольшего общего делителя
        """
    if b == 0:
        return a
    if b > a:
        a, b = b, a

    return gcd_recursive_computation(a - b, b)


def gcd_iterative_slow(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух целых чисел.
    Медленная итеративная реализация

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    :return: значение наибольшего общего делителя
    """
    a, b = gcd_helper(a, b)

    while b != 0:
        a, b = a - b, b
        if b > a:
            a, b = b, a
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
    a, b = gcd_helper(a, b)

    while b != 0:
        a, b = b, a % b
    return a


def gcd_validate(a: int, b: int):
    """Проверяет выполнения необходимых условий для вычисления НОД чисел a и b

    :param a: целое число a
    :param b: целое число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    """
    if type(a) != int:
        raise Exception("Значение параметра a не является целым числом")

    if type(b) != int:
        raise Exception("Значение параметра b не является целым числом")

    if a == 0 and b == 0:
        raise Exception("Значения параметров a и b равны нулю")


def gcd_helper(a: int, b: int):
    """Вспомогательная функция для вычисления НОД с помощью итеративного метода, для того чтобы не писать одинаковые
     куски кода в медленной и быстрой версиях.
     Функция проверяет числа a и b на выполнение необходимых условий, берет модули от чисел (не влияет на вычисление
     НОД) и приводит числа к виду, что a - большее из двух чисел, b - соответственно меньшее

    :param a:
    :param b:
    :return:
    """
    gcd_validate(a, b)
    a = abs(a)
    b = abs(b)

    if b > a:
        a, b = b, a

    return a, b


def lcm(a: int, b: int) -> int:
    """Вычисляет наименьшее общее кратное двух натуральных чисел

    :param a: натуральное число a
    :param b: натуральное число b
    :raise Exception: если a или b не являются натуральными числами или
    они равны нулю
    :return: значение наименьшего общего кратного
    """
    lcm_validate(a, b)
    return int(a * b / gcd_iterative_fast(a, b))


def lcm_validate(a: int, b: int):
    """Проверяет выполнения необходимых условий для вычисления НОК чисел a и b

    :param a: натуральное число a
    :param b: натуральное число b
    :raise Exception: если a или b не являются целыми числами или
    они оба равны нулю
    """
    if type(a) != int or a < 1:
        raise Exception("Значение параметра a не является натуральным положительным числом")

    if type(b) != int or b < 1:
        raise Exception("Значение параметра b не является натуральным положительным числом")


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
