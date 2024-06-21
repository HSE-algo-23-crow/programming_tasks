ERR_EMPTY_BOTH_STRINGS = "Начальная строка и искомая подстрока являются пустыми."
ERR_EMPTY_INIT_STRING = "Начальная строка является пустой."
ERR_EMPTY_SUBSTRING = "Искомая подстрока является пустой."
ERR_SUBSTRING_LARGE_THAN_INIT_STRING = "Искомая подстрока больше начальной подстроки."


def __get_valid_params(substring: str, init_string: str):
    """Валидация параметров.

    :param substring: Искомая подстрока.
    :param init_string: Начальная строка, в которой будет осуществляться поиск подстроки.
    :raise ValueError: Если искомая подстрока или начальная строка является пустой,
     или если подстрока больше начальной строки
    """

    if len(init_string) == 0 and len(substring) == 0:
        raise ValueError(ERR_EMPTY_BOTH_STRINGS)

    if len(init_string) == 0:
        raise ValueError(ERR_EMPTY_INIT_STRING)

    if len(substring) == 0:
        raise ValueError(ERR_EMPTY_SUBSTRING)

    if len(substring) > len(init_string):
        raise ValueError(ERR_SUBSTRING_LARGE_THAN_INIT_STRING)


def substring_search(substring: str, init_string: str) -> int:
    """Алгоритм Бойера-Мура-Хорспула: оптимальный поиск подстроки в строке.

    :param substring: Искомая подстрока.
    :param init_string: Начальная строка, в которой будет осуществляться поиск подстроки.
    :return: Индекс начала первого вхождения подстроки или -1, если подстрока не найдена.
    """

    # Валидация параметров
    __get_valid_params(substring, init_string)

    # Формирование таблицы смещений
    uniq_symbols = set()
    len_sub = len(substring)
    offsets = {}

    for i in range(len_sub - 2, -1, -1):
        if substring[i] not in uniq_symbols:
            offsets[substring[i]] = len_sub - i - 1
            uniq_symbols.add(substring[i])

    if substring[len_sub - 1] not in uniq_symbols:
        offsets[substring[len_sub - 1]] = len_sub

    offsets["*"] = len_sub

    # Поиск подстроки в строке
    len_init = len(init_string)
    i = len_sub - 1

    while i < len_init:
        k = 0
        flag = False

        for j in range(len_sub - 1, -1, -1):
            if init_string[i - k] != substring[j]:
                if j == len_sub - 1:
                    off = offsets[init_string[i]] if offsets.get(init_string[i], False) else offsets["*"]
                else:
                    off = offsets[substring[j]]

                i += off
                flag = True
                break

            k += 1

        if not flag:
            return i - k + 1

    else:
        return -1


def main():
    init_string = "Сын «пятого битла» тоже продюсировал музыку The Beatles."
    substring = "тоже"

    index = substring_search(substring, init_string)

    print("Пример поиска подстроки в строке алгоритмом Бойера-Мура-Хорспула\n")
    print(f"Начальная строка: {init_string}")
    print(f"Искомая подстрока: {substring}\n")

    if not(index == -1):
        print(f"Искомая подстрока найдена по индексу: {index}")
    else:
        print(f"Данная подстрока отсутствует в начальной строке")


if __name__ == '__main__':
    main()
