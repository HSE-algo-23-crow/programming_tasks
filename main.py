def minor(matrix, row, col):
    """Функция для получения подматрицы без заданной строки и столбца."""
    return [[matrix[i][j] for j in range(len(matrix[i])) if j != col] for i in range(len(matrix)) if i != row]
def calculate_determinant(matrix: [[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы
    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    """Функция для вычисления определителя матрицы с использованием рекурсии."""
    for row in matrix:
        if type(row) != list:
            raise ValueError("Ошибка, введен не список")
        if len(row) != len(matrix):
            raise ValueError("Матрица не квадратная")
    n = len(matrix)
    if n == 0:
        raise ValueError("Матрица не пустая")
    # Базовый случай: если матрица 1x1, вернуть ее единственный элемент
    if n == 1:
        return matrix[0][0]
    # Базовый случай: если матрица 2x2, вернуть определитель по формуле ad - bc
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        # Рекурсивно вычисляем определитель для каждого элемента первой строки
        for i in range(n):
            det += ((-1) ** i) * matrix[0][i] * calculate_determinant(minor(matrix, 0, i))
        return det


def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print('Матрица')
    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')


if __name__ == '__main__':
    main()
