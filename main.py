from itertools import permutations
from permutations import generate_permutations

NullableNumber = int | float | None

INFINITY = float('inf')
DISTANCE = 'distance'
PATH = 'path'
PARAM_ERR_MSG = ('Таблица расстояний не является прямоугольной матрицей с '
                 'числовыми значениями')
NEG_VALUE_ERR_MSG = 'Расстояние не может быть отрицательным'
MAX_TOWNS = 10


def get_salesman_path(dist_matrix: list[list[NullableNumber]]) -> \
        dict[str, float | list[int]]:
    """Решает задачу коммивояжёра с использованием полного перебора.

    :param dist_matrix: Матрица расстояний.
    :raise TypeError: Если таблица расстояний не является прямоугольной
    матрицей с числовыми значениями.
    :raise ValueError: Если в матрице присутствует отрицательное значение.
    :return: Словарь с ключами: distance - кратчайшее расстояние,
    path - список с индексами вершин на кратчайшем маршруте.
    """

    if not isinstance(dist_matrix, list) or not all(isinstance(row, list) for row in dist_matrix):
        raise TypeError(PARAM_ERR_MSG)

    size = len(dist_matrix)

    if size == 0 or any(len(row) != size for row in dist_matrix):
        raise TypeError(PARAM_ERR_MSG)

    for row in dist_matrix:
        for value in row:
            if value is not None and not isinstance(value, (int, float)):
                raise TypeError(PARAM_ERR_MSG)
            if value is not None and value < 0:
                raise ValueError(NEG_VALUE_ERR_MSG)

    if size > MAX_TOWNS:
        raise ValueError(f'Количество городов превышает допустимое значение ({MAX_TOWNS})')

    # Обработка случая единичного порядка
    if size == 1:
        return {DISTANCE: 0, PATH: [0]}

    min_path_length = INFINITY
    best_path = []

    for perm in permutations(range(size)):
        current_length = 0
        valid_path = True

        for i in range(size):
            src = perm[i]
            trg = perm[(i + 1) % size]

            if dist_matrix[src][trg] is None:
                valid_path = False
                break

            current_length += dist_matrix[src][trg]

        if valid_path and current_length < min_path_length:
            min_path_length = current_length
            best_path = list(perm) + [perm[0]]

    if best_path:
        return {DISTANCE: min_path_length, PATH: best_path}
    else:
        return {DISTANCE: None, PATH: []}


# Пример использования
if __name__ == '__main__':
    print('Пример решения задачи коммивояжёра\n\nМатрица расстояний:')
    matrix = [[1., 2., 3., 4.],
                  [5., 6., 7., 8.],
                  [9., 10., 11., 12.],
                  [13., 14., 15., 16.]]
    for row in matrix:
        print(row)

    print('\nРешение задачи:')
    print(get_salesman_path(matrix))