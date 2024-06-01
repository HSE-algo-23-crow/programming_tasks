ERR_NOT_LIST_MSG = 'Переданный параметр не является списком'
ERR_EMPTY_LIST_MSG = 'Переданный список пуст'
ERR_NOT_INT_TEMPL = 'Элемент списка [{0}] не является целым числом'
ERR_NOT_START_WITH_1_MSG = 'Список не начинается с 1'
ERR_HAS_DUPLICATES_MSG = 'Список содержит дубликаты'
ERR_OVER_CONSTRAINT_TEMPL = ('Значение [{0}] в позиции [{1}] превышает '
                             'ограничение n - i + 1')


def ENCODE_VERIFY(numbers: list[int]) -> None|Exception:
    if type(numbers) is not list: raise TypeError(ERR_NOT_LIST_MSG)
    if not len(numbers): raise ValueError(ERR_EMPTY_LIST_MSG)
    if type(numbers[0]) is int:
        if numbers[0] != 1: raise ValueError(ERR_NOT_START_WITH_1_MSG)
    else: raise TypeError(ERR_NOT_INT_TEMPL.format(numbers[0]))
    for index in range(len(numbers)):
        if type(numbers[index]) is not int: raise TypeError(ERR_NOT_INT_TEMPL.format(numbers[index]))
        if numbers.count(numbers[index]) > 1: raise ValueError(ERR_HAS_DUPLICATES_MSG)


def encode(numbers: list[int]) -> list[int]:
    """Переводит решение задачи коммивояжера из натуральной кодировки в
    альтернативную. Решение всегда начинается с единицы.
        :param numbers: Натуральная кодировка решения - список целых
        положительных чисел.
        :raise TypeError: Если переданный параметр не является списком целых
        положительных чисел.
        :raise ValueError: Если список содержит дубликаты или не начинается с
        единицы.
        :return: Альтернативная кодировка решения - список целых
        положительных чисел.
        """

    ENCODE_VERIFY(numbers)

    result = []
    help = [i+1 for i in range(len(numbers))]
    while len(help) > 0:
        result.append(help.index(numbers[0]) + 1)
        help.pop(help.index(numbers[0]))
        numbers.pop(0)
    return result


def DECODE_VERIFY(codes: list[int]) -> None|Exception:
    if type(codes) is not list: raise TypeError(ERR_NOT_LIST_MSG)
    if not len(codes): raise ValueError(ERR_EMPTY_LIST_MSG)
    if type(codes[0]) is int:
        if codes[0] != 1: raise ValueError(ERR_NOT_START_WITH_1_MSG)
    else:
        raise TypeError(ERR_NOT_INT_TEMPL.format(codes[0]))
    for index in range(len(codes)):
        if codes[index] > len(codes) - index: raise ValueError(ERR_OVER_CONSTRAINT_TEMPL.format(codes[index], index + 1))
        if type(codes[index]) is not int: raise TypeError(ERR_NOT_INT_TEMPL.format(codes[index]))



def decode(codes: list[int]) -> list[int]:
    """Переводит решение задачи коммивояжера из альтернативной кодировки в
    натуральную.
        :param numbers: Альтернативная кодировка решения - список целых
        положительных чисел.
        :raise TypeError: Если переданный параметр не является списком целых
        положительных чисел.
        :raise ValueError: Если список не начинается с единицы или нарушено
        ограничение (n - i + 1).
        :return: Натуральная кодировка решения - список целых
        положительных чисел.
        """

    DECODE_VERIFY(codes)

    help = [i+1 for i in range(len(codes))]
    result = []
    for code in codes:
        result.append(help[code-1])
        help.pop(code-1)
    return result


if __name__ == '__main__':
    print('Пример натуральной и альтернативной кодировки решения задачи о '
          'рюкзаке\n')
    natural = [1, 7, 4, 3, 8, 6, 2, 5]
    alter = [1, 1, 1, 2, 1]
    print(f'Натуральный код {natural} -> Альтернативный код {encode(natural)}')
    print(f'Альтернативный код {alter} -> Натуральный код {decode(alter)}')