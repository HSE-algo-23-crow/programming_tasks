def calculate_determinant(matrix):
    # Проверяем, не является ли матрица пустой
    if not matrix:
        raise Exception("Матрица пустая")

    # Получаем количество строк (и столбцов) в матрице (предполагается, что матрица квадратная)
    n = len(matrix)

    # Проверяем, является ли матрица квадратной (все строки имеют одинаковую длину)
    for row in matrix:
        if len(row) != n:
            raise Exception("Матрица не квадратная")

    # Базовый случай рекурсии: определитель 1x1 матрицы равен ее единственному элементу
    if n == 1:
        return matrix[0][0]

    determinant = 0

    # Вычисление определителя методом разложения по первой строке
    for j in range(n):
        # Вычисляем алгебраическое дополнение элемента matrix[0][j]

        # Создаем минор, удаляя первую строку и j-ый столбец
        minor = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]

        # Вычисляем значение алгебраического дополнения
        cofactor = matrix[0][j] * calculate_determinant(minor)

        # Переменно меняем знак для четных и нечетных j
        if j % 2 == 0:
            determinant += cofactor
        else:
            determinant -= cofactor

    return determinant


def main():
    # Примеры матриц разных порядков и вычисление их определителей

    # Матрица 2x2
    matrix = [[1, 2],
              [3, 4]]
    print('Матрица')
    for row in matrix:
        print(row)
    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')

    # Матрица 3x3
    matrix_3x3 = [[1, -2, 3],
                  [-4, 5, -6],
                  [7, -8, 9]]
    print('\nМатрица 3x3')
    for row in matrix_3x3:
        print(row)
    print(f'Определитель матрицы 3x3 равен {calculate_determinant(matrix_3x3)}')

    # Матрица 4x4
    matrix_4x4 = [[3, -3, -5, 8],
                  [-3, 2, 4, -6],
                  [2, -5, -7, 5],
                  [-4, 3, 5, -6]]
    print('\nМатрица 4x4')
    for row in matrix_4x4:
        print(row)
    print(f'Определитель матрицы 4x4 равен {calculate_determinant(matrix_4x4)}')

    # Матрица 5x5
    matrix_5x5 = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
    print('\nМатрица 5x5')
    for row in matrix_5x5:
        print(row)
    print(f'Определитель матрицы 5x5 равен {calculate_determinant(matrix_5x5)}')


if __name__ == '__main__':
    main()
