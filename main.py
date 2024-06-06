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
    elif numbers[0] != 1:
        raise ValueError(ERR_NOT_START_WITH_1_MSG)
    else:
        for item in numbers:
            if not isinstance(item, int):
                raise TypeError(ERR_NOT_INT_TEMPL)

def encode_validation(numbers: list[int]):
    if not isinstance(numbers, list):
        raise TypeError(ERR_NOT_LIST_MSG)
    elif len(numbers) == 0:
        raise ValueError(ERR_EMPTY_LIST_MSG)
    elif numbers[0] != 1:
        raise ValueError(ERR_NOT_START_WITH_1_MSG)
    elif len(numbers) != len(set(numbers)):
        raise ValueError(ERR_HAS_DUPLICATES_MSG)
    else:
        for item in numbers:
            if not isinstance(item, int):
                raise TypeError(ERR_NOT_INT_TEMPL)
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

    return numbers


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
    return codes


if __name__ == '__main__':
    print('Пример натуральной и альтернативной кодировки решения задачи о '
          'рюкзаке\n')
    natural = [1, 5, 2, 4, 3]
    alter = None
    print(f'Натуральный код {natural} -> Альтернативный код {encode(natural)}')
    print(f'Альтернативный код {alter} -> Натуральный код {decode(alter)}')