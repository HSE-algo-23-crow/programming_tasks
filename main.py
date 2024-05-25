ERR_NOT_LIST_MSG = 'Переданный параметр не является списком'
ERR_EMPTY_LIST_MSG = 'Переданный список пуст'
ERR_NOT_INT_TEMPL = 'Элемент списка [{0}] не является целым числом'
ERR_NOT_START_WITH_1_MSG = 'Список не начинается с 1'
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
    _check_encode_params(numbers)
    result = []
    while len(numbers) > 0:
        sorted_numbers = sorted(numbers)
        current_number = numbers[0]
        current_number_index = sorted_numbers.index(current_number)
        result.append(current_number_index + 1)
        numbers.pop(0)
    return result


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
    _check_decode_params(codes)
    numbers = [i+1 for i in range(len(codes))]
    result  = []
    for ind in codes:
        current_number = numbers[ind-1]
        result.append(current_number)
        numbers.pop(ind -1)
    return result




def _check_decode_params(codes: list[int]):
    _check_list_type(codes)
    for i in range(len(codes)):
        c = codes[i]
        _check_param_type(c)
        if (i == 0 and c != 1):
            raise ValueError(ERR_NOT_START_WITH_1_MSG)
        if (c > len(codes) - i):
            raise ValueError(ERR_OVER_CONSTRAINT_TEMPL.format(c, i+1))


def _check_param_type(code: int):
    if (type(code) != int):
        raise TypeError(ERR_NOT_INT_TEMPL.format(code))


def _check_list_type(lst):
    if (type(lst) != list):
        raise TypeError(ERR_NOT_LIST_MSG)

    if len(lst) == 0:
        raise ValueError(ERR_EMPTY_LIST_MSG)


def _check_encode_params(codes: list[int]):
    _check_list_type(codes)
    for i in range(len(codes)):
        c = codes[i]
        _check_param_type(c)
        if (i == 0 and c != 1):
            raise ValueError(ERR_NOT_START_WITH_1_MSG)
        if codes.count(c) > 1:
            raise ValueError(ERR_HAS_DUPLICATES_MSG)


if __name__ == '__main__':
    print('Пример натуральной и альтернативной кодировки решения задачи о '
          'рюкзаке\n')
    natural = [1, 5, 2, 4, 3]
    alter = [1, 1, 1, 2, 1]
    print(f'Натуральный код {natural} -> Альтернативный код {encode(natural)}')
    print(f'Альтернативный код {alter} -> Натуральный код {decode(alter)}')
