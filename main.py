def calculate_determinant(matrix: [[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    validate_matrix_raises_ex(matrix)

    if len(matrix) == 1:
        return matrix[0][0]

    row_index = choose_optimal_row_ind(matrix)
    det = 0

    for col_ind in range(len(matrix)):
        if matrix[row_index][col_ind] == 0:
            continue
        det += matrix[row_index][col_ind] * (-1) ** (row_index + col_ind) * calculate_minor(matrix, row_index, col_ind)

    return det


def choose_optimal_row_ind(matrix: [[int]]) -> int:
    optimal_index = 0
    max_zero_counter = 0
    for i in range(len(matrix)):
        zero_counter = sum(1 for x in matrix[i] if x == 0)
        if zero_counter > max_zero_counter:
            optimal_index = i
            max_zero_counter = zero_counter
    return optimal_index


def validate_matrix_raises_ex(matrix: [[int]]):
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError()
    len_matrix = len(matrix)
    for row in matrix:
        if type(row) != list:
            raise TypeError()
        if len(row) != len_matrix:
            raise ValueError()


def calculate_minor(matrix: [[int]], row_ind: int, col_ind: int) -> int:
    reduced_matrix = []
    for i in range(len(matrix)):
        if i == row_ind: continue
        new_row = []
        for j in range(len(matrix)):
            if j == col_ind:
                continue
            else:
                new_row.append(matrix[i][j])
        reduced_matrix.append(new_row)

    return calculate_determinant(reduced_matrix)


def main():
    matrix = [[1, 2],
              [3, 4]]
    print('Матрица')
    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')


if __name__ == '__main__':
    main()
