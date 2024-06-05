ERR_NOT_LIST_MSG = 'Переданный параметр не является списком'
ERR_EMPTY_LIST_MSG = 'Переданный список пуст'
ERR_NOT_INT_TEMPL = 'Элемент списка [{0}] не является целым числом'
ERR_NOT_START_WITH_0_MSG = 'Список не начинается с 0-го индекса'
ERR_HAS_DUPLICATES_MSG = 'Список содержит дубликаты'
ERR_OVER_CONSTRAINT_TEMPL = ('Значение [{0}] в позиции [{1}] превышает '
                             'ограничение n - i + 1')

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
    if not (isinstance(numbers, list)):
        raise TypeError(ERR_NOT_LIST_MSG)

    if not (numbers):
        raise ValueError(ERR_EMPTY_LIST_MSG)

    if not (all(isinstance(item, int) for item in numbers)):
        for item in numbers:
            if not (isinstance(item, int)):
                raise TypeError(ERR_NOT_INT_TEMPL.format(item))

    if numbers[0] != 0:
        raise ValueError(ERR_NOT_START_WITH_0_MSG)

    if len(numbers) != len(set(numbers)):
        raise ValueError(ERR_HAS_DUPLICATES_MSG)

    encoded_arr = []
    remaining_arr = []
    for i in range(0, len(numbers)):
        remaining_arr.append(i)

    for item in numbers:
        index = remaining_arr.index(item)
        encoded_arr.append(index)
        remaining_arr.pop(index)

    return encoded_arr


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
    if not (isinstance(codes, list)):
        raise TypeError(ERR_NOT_LIST_MSG)

    if not (codes):
        raise ValueError(ERR_EMPTY_LIST_MSG)

    if not (all(isinstance(code, int) for code in codes)):
        for item in codes:
            if not (isinstance(item, int)):
                raise TypeError(ERR_NOT_INT_TEMPL.format(item))

    if codes[0] != 0:
        raise ValueError(ERR_NOT_START_WITH_0_MSG)

    decoded_arr = []
    remaining_arr = []
    for i in range(len(codes)):
        remaining_arr.append(i)

    for i, item in enumerate(codes):
        if item > len(codes) - i:
            raise ValueError(ERR_OVER_CONSTRAINT_TEMPL.format(item, i + 1))
        decoded_arr.append(remaining_arr[item])
        remaining_arr.pop(item)

    return decoded_arr


if name == 'main':
    print('Пример натуральной и альтернативной кодировки решения задачи о '
          'рюкзаке\n')
    natural = [0, 4, 1, 3, 2]
    alter = [0, 0, 0, 1, 0]
    print(f'Натуральный код {natural} -> Альтернативный код {encode(natural)}')
    print(f'Альтернативный код {alter} -> Натуральный код {decode(alter)}')