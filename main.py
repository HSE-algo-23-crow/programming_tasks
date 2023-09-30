def calculate_determinant(matrix: [[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :return: значение определителя
    """
    validate_square_matrix(matrix)
    return calculate_determinant_recursion(matrix)


def calculate_determinant_recursion(matrix: [[int]]) -> int:
    """"Считает определитель, основная функция с рекурсией
    param matrix: целочисленная квадратиная матрица
    :return: значение определителя
    """

    if len(matrix) == 1:
        return matrix[0][0]

    determinant = 0

    optimal_row_index = choose_optimal_row_index(matrix)

    for column_index in range(0, len(matrix)):
        if matrix[optimal_row_index][column_index] == 0:
            continue
        else:
            determinant += matrix[optimal_row_index][column_index] * (-1) ** (column_index + optimal_row_index) * calculate_minor(matrix, column_index, optimal_row_index)
    return determinant


def calculate_minor(matrix: [[int]], matrix_column_index, optimal_row_index):
    """"Находит определитель минора через рекурсию
    param matrix: целочисленная квадратиная матрица
    param matrix_column_index
    :return: значение определителя
    """

    minor = []

    for row_index in range(0, len(matrix)):

        if row_index == optimal_row_index:
            continue

        else:
            minor_row = []

            for column_index in range(0, len(matrix)):

                if column_index == matrix_column_index:
                    continue

                else:
                    minor_row.append(matrix[row_index][column_index])
        minor.append(minor_row)
    return calculate_determinant_recursion(minor)


def choose_optimal_row_index(matrix: [[int]]) -> int:
    max_zero_number = 0
    optimal_row_index = 0
    row_index = 0

    for row in matrix:
        zero_counter = 0
        for i in range(0, len(row)):

            if row[i] == 0:
                zero_counter += 1

        if zero_counter > max_zero_number:
            optimal_row_index = row_index

        row_index += 1
    return optimal_row_index


def validate_square_matrix(matrix: [[int]]):
    """Проверяет параметр на корректность ввода
    :param matrix: введённое значение, которое может быть или не быть матрицей
    :raise ValueError: если значение параметра не является целочисленной квадратной матрицей"""

    if type(matrix) != list:
        raise ValueError('Неверный тип данных значения матрицы!')
    elif len(matrix) == 0:
        raise ValueError('Матрица не может быть пустой')

    row_counter = 0
    for row in matrix:
        row_counter += 1

        if len(matrix) != len(row):
            raise ValueError('Матрица не является квадратной!')

        for i in range(0, len(row)):

            if type(row[i]) != int:
                raise ValueError('Один или несколько элементов матрицы не являются целым числом!')


def main():
    matrix = [[1, 2],
              [3, 4]]
    print('Матрица')

    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')


if __name__ == '__main__':
    main()
