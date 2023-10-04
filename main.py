import numpy


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


def calculate_minor(matrix, row_idx, column_idx):
    minor = numpy.delete(numpy.delete(matrix, row_idx, axis=0), column_idx, axis=1)
    return minor


def choose_optimal_row_idx():
    pass


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
    matrix = [[1, 2],
              [3, 4]]
    print('Матрица')
    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')


if __name__ == '__main__':
    main()
