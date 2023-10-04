def calculate_determinant(matrix: [[int]]) -> int:
    """Функция-обертка включает в себя проверку матрицы на выполнения необходимых условий и вызов функции-вычислителя

    :param matrix: введенная матрица (может быть и не матрицей)
    :return: значения определителя (через функцию-вычислитель)
    """
    validate_matrix_raises_ex(matrix)  # Проверка выполнения необходимых условий для матрицы
    return calculate_determinant_computation(matrix)


def calculate_determinant_computation(matrix: [[int]]) -> int:
    """Функция-вычислитель - вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :return: значение определителя
    """
    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    row_index = choose_optimal_row_index(matrix)

    for col_index in range(len(matrix)):
        if matrix[row_index][col_index] == 0:
            continue
        else:
            det += ((matrix[row_index][col_index] * (-1) ** (row_index + col_index + 2)) *
                    calculate_minor(matrix, row_index, col_index))

    return det


def validate_matrix_raises_ex(matrix):
    """Проверяет выполнения необходимых условий для матрицы (проверка на целочисленную квадратную матрицу)

    :param matrix: полученная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    """
    if type(matrix) != list or len(matrix) == 0:
        # Введенные данные не список => не матрица
        raise ValueError('Ошибка типизации. Введенные данные нельзя представить в виде матрицы.')

    order = len(matrix)
    for row in matrix:
        if type(row) != list:
            # Если элементы списка не являются списками => не матрица
            raise ValueError('Ошибка типизации. Введенный список нельзя представить в виде матрицы.')
        if len(row) != order:
            # Если кол-во элементов не равно кол-ву строк => не квадратная матрица
            raise ValueError('Ошибка. Введенные данные нельзя представить в виде целочисленной квадратной матрицы.')


def choose_optimal_row_index(matrix: [[int]]) -> int:
    """Определяет индекс строки с наибольшим количеством нулей для дальнейшего оптимального вычисления

    :param matrix: целочисленная квадратная матрица
    :return: значения индекса строки для дальнейшего оптимального вычисления
    """
    row_index = 0
    optimal_row_index = row_index
    max_zero_count = 0

    for row in matrix:
        zero_count = 0

        for value in range(len(row)):
            if row[value] == 0:
                zero_count += 1

        if zero_count > max_zero_count:
            optimal_row_index = row_index

        row_index += 1

    return optimal_row_index


def calculate_minor(matrix: [[int]], row_index, col_index):
    """Находит определитель минора с помощью рекурсивного метода

    :param matrix: целочисленная квадратная матрица
    :param row_index: индекс строки матрицы
    :param col_index: индекс столбца матрицы
    :return:
    """
    minor = []

    for row_ind in range(len(matrix)):
        if row_ind == row_index:
            continue
        else:
            minor_row = []

            for col_ind in range(len(matrix)):
                if col_ind == col_index:
                    continue
                else:
                    minor_row.append(matrix[row_ind][col_ind])

        minor.append(minor_row)

    return calculate_determinant_computation(minor)


def main():
    matrix = [[1, 2],
              [3, 4]]

    print('Матрица')
    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')


if __name__ == '__main__':
    main()
