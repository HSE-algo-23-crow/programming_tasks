import time


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    "первый и текущий элемент последовательности до n"
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def rabbits(month: int, lifetime: int) -> int:
    """Возвращает количество пар кроликов в популяции на заданный месяц.
    В начальный момент времени имеется одна пара кроликов. Начиная со второго
    месяца после рождения кролики производят новую пару кроликов каждый месяц.
    После достижения предельного возраста кролики умирают.

    :param month: количество месяцев жизни популяции
    :param lifetime: продолжительность жизни кролика, не менее 2 месяцев
    :return: количество пар кроликов
    """

    if month <= 0 or lifetime < 2:  # проверка корректности входных параметров
        return 0
    pairs = 1  # начальное количество пар кроликов
    age = 1  # начальный возраст кроликов

    for _ in range(2, month + 1):
      new_pairs = pairs  # новые родившиеся пары
      if age >= 2:  # кролик достиг возраста размножения
         new_pairs = pairs + new_pairs

      age += 1  # увеличение возраста всех кроликов
      if age > lifetime:  # удаление умерших кроликов
         pairs -= 1

      pairs = new_pairs  # обновление количества пар кроликов

    return pairs


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
