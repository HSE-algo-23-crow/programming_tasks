ERR_NOT_LIST_MSG = 'Переданный параметр не является списком'
ERR_EMPTY_LIST_MSG = 'Переданный список пуст'
ERR_NOT_INT_TEMPL = 'Элемент списка [{0}] не является целым числом'
ERR_NOT_START_WITH_1_MSG = 'Список не начинается с 1'
ERR_HAS_DUPLICATES_MSG = 'Список содержит дубликаты'
ERR_OVER_CONSTRAINT_TEMPL = ('Значение [{0}] в позиции [{1}] превышает '
                             'ограничение n - i + 1')

def decode_validation(numbers: list[int]):
    if not isinstance(numbers, list):
        raise TypeError(ERR_NOT_LIST_MSG)
    elif len(numbers) == 0:
        raise ValueError(ERR_EMPTY_LIST_MSG)
    else:
        for item in numbers:
            if not isinstance(item, int):
                raise TypeError(ERR_NOT_INT_TEMPL.format(item))
    if numbers[0] != 1:
        raise ValueError(ERR_NOT_START_WITH_1_MSG)
    for i in range(len(numbers)):
        if numbers[i] >= len(numbers) - i + 1:
            raise ValueError(ERR_OVER_CONSTRAINT_TEMPL.format(numbers[i], i + 1))

def encode_validation(numbers: list[int]):
    if not isinstance(numbers, list):
        raise TypeError(ERR_NOT_LIST_MSG)
    elif len(numbers) == 0:
        raise ValueError(ERR_EMPTY_LIST_MSG)
    else:
        for item in numbers:
            if not isinstance(item, int):
                raise TypeError(ERR_NOT_INT_TEMPL.format(item))
    if numbers[0] != 1:
        raise ValueError(ERR_NOT_START_WITH_1_MSG)
    elif len(numbers) != len(set(numbers)):
        raise ValueError(ERR_HAS_DUPLICATES_MSG)

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
    encode_validation(numbers)

    sort_numbers = sorted(numbers)
    encoded_numbers = []
    for i in range(len(numbers)):
        index = sort_numbers.index(numbers[0]) + 1
        encoded_numbers.append(index)
        numbers.pop(0)
        sort_numbers.pop(index - 1)
    return encoded_numbers


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
    decode_validation(codes)

    sort_codes = [i for i in range(len(codes))]
    decoded_numbers = []
    for i in range(len(codes)):
        item = sort_codes[codes[0] - 1] + 1
        decoded_numbers.append(item)
        sort_codes.pop(codes[0] - 1)
        codes.pop(0)
    return decoded_numbers

if __name__ == '__main__':
    print('Пример натуральной и альтернативной кодировки решения задачи о '
          'рюкзаке\n')
    natural = [1, 3, 5, 4, 2, 7, 6]
    alter = [1, 2, 3, 2, 1, 2, 1]
    print(f'Натуральный код {natural} -> Альтернативный код {encode(natural)}')
    print(f'Альтернативный код {alter} -> Натуральный код {decode(alter)}')