def calculate_determinant(_matrix: [[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param _matrix: Целочисленная квадратная матрица
    :raise Exception: Если значение параметра не является целочисленной
    квадратной матрицей
    :return: Значение определителя
    """
    square_matrix_check(_matrix)

    if len(_matrix) == 1:
        return _matrix[0][0]

    row_idx = choose_optimal_row_idx(_matrix)

    det = 0
    for column_idx in range(len(_matrix)):
        if _matrix[row_idx][column_idx] == 0:
            continue
        det += _matrix[row_idx][column_idx] * (-1) ** (row_idx + column_idx) * calculate_minor(_matrix, row_idx,
                                                                                               column_idx)
    return det


def calculate_minor(_matrix, _row_idx, _column_idx):
    """Вычисляет минор целочисленной квадратной матрицы и создать матрицу на основе этого минора

    :param _column_idx: Индекс столбца
    :param _row_idx: Индекс строки
    :param _matrix: Целочисленная квадратная матрица
    :raise Exception: Если значение параметра не является целочисленной
    квадратной матрицей
    :return: Рекурсивный метод вычисления определителя
    """
    minor = []
    for i in range(len(_matrix)):
        if i != _row_idx:
            minor_row = []
            for j in range(len(_matrix)):
                if j != _column_idx:
                    minor_row.append(_matrix[i][j])
            minor.append(minor_row)
    return calculate_determinant(minor)


def choose_optimal_row_idx(_matrix):
    for i in range(0, 2):
        if 0 in _matrix[i]:
            return i
    return 0


def square_matrix_check(_matrix):
    """ Вычисляет минор целочисленной квадратной матрицы

    :param _matrix: Целочисленная квадратная матрица?
    :raise Exception: Если значение параметра не является целочисленной
    квадратной матрицей
    :return:
    """
    if type(_matrix) != list:
        raise Exception("Введенное значение не является списком!")
    for row in _matrix:
        if type(row) != list:
            raise Exception("Введенное значение не является вложенным списком!")
        if len(row) != len(_matrix):
            raise Exception("Введенное значение не является квадратной матрицей!")
        for ind in row:
            if type(ind) != int:
                raise Exception("Значения в квадратной матрице не является целочисленными!")


def main():
    matrix = [[1, 2, 0],
              [3, 4, 2],
              [1, 4, 6]]
    print('Матрица')
    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')


if __name__ == '__main__':
    main()
