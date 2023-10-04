
def determinant(matrix: [[int]]) -> int:
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    det = 0

    for col in range(len(matrix)):
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        sign = 1-(col % 2)*2
        det += sign * matrix[0][col] * determinant(submatrix)

    return det


def calculate_determinant(matrix: [[int]]) -> int:
    check(matrix)

    return determinant(matrix)


def check(matrix: [[int]]) -> None:
    if type(matrix) != list:
        raise ValueError("Вводные данные должны быть списком")
    if False in [type(i) == list for i in matrix]:
        raise ValueError("Вводные данные должны быть двумерным списком")
    if len(matrix) != len(matrix[0]):
        raise ValueError("Вводная матрица должна быть квадратной")
    if False in [(type(i) in [int, float] for i in j) for j in matrix]:
        raise ValueError("Вводные данные должны состоять из чисел")


def main():
    matrix = [[10, 4, 1],
              [5, 6, 7],
              [9, 10, 5]]
    print('Матрица')
    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {determinant(matrix)}')


if __name__ == '__main__':
    main()
