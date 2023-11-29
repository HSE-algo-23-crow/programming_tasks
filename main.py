STR_LENGTH_ERROR_MSG = 'Длина строки должна быть целым положительным числом'
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = 'Параметр {0} Не является целым числом'
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = 'Параметр {0} отрицательный'
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = 'Параметр n меньше чем k'
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.
    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    if type(length) != int or length < 1:
        raise ValueError(STR_LENGTH_ERROR_MSG)
    string = ''
    lst = []
    if length == 0:
        return lst
    insert_zero(string, length, lst)
    insert_one(string, length, lst)
    return lst


def insert_zero(string, ln, lst):
    if len(string) == ln-1:
        lst.append('0' + string)
    else:
        insert_one('0' + string, ln, lst)


def insert_one(string, ln, lst):
    if len(string) == ln-1:
        lst.append('1' + string)
    else:
        insert_zero('1' + string, ln, lst)
        insert_one('1' + string, ln, lst)


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    check_error = __check_params(n, k)
    if check_error:
        raise ValueError(check_error)
    if use_rec:
        return bin_rec(n, k)
    return bin_iter(n, k)


def __check_params(n: int, k: int) -> dict[str: bool, str: str]:
    for param, param_name in zip([n, k], ['n', 'k']):
        if type(param) != int:
            return NOT_INT_VALUE_TEMPL.format(param_name)
        if param < 0:
            return NEGATIVE_VALUE_TEMPL.format(param_name)
    if n < k:
        return N_LESS_THAN_K_ERROR_MSG


def bin_iter(n: int, k: int) -> int:
    if n == k or k == 0:
        return 1
    pascal_triangle = [[1]] + [[1] + ([0] * i) + [1] for i in range(n)]
    for i in range(2, n + 1):
        for j in range(1, n):
            if j < i:
                pascal_triangle[i][j] = pascal_triangle[i - 1][j] + \
                                        pascal_triangle[i - 1][j - 1]
    return pascal_triangle[n][k]


def bin_rec(n: int, k: int) -> int:
    if n == k or k == 0:
        return 1
    return bin_rec(n - 1, k) + bin_rec(n - 1, k - 1)


def main():
    n = 10
    print(f'Строки длиной {n}:\n{generate_strings(n)}')

    n = 30
    k = 20
    print(f'Биномиальный коэффициент (итеративно) при n, k ({n}, {k}) = ',
          binomial_coefficient(n, k))
    print(f'Биномиальный коэффициент (рекурсивно) при n, k ({n}, {k}) = ',
          binomial_coefficient(n, k, use_rec=True))


if __name__ == '__main__':
    main()
