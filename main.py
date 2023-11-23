def calculate_determinant(matrix):
    # Проверяем, является ли матрица квадратной
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Матрица не является квадратной")

    # Базовый случай: если матрица 1x1, то ее определитель равен единственному элементу
    if len(matrix) == 1:
        return matrix[0][0]

    determinant = 0
    for i in range(len(matrix)):
        # Вычисляем минор (удаляем i-ю строку и 0-й столбец)
        minor = [row[1:] for row in (matrix[:i] + matrix[i + 1:])]

        # Вычисляем знак, который зависит от четности суммы индексов строки и столбца
        sign = (-1) ** i

        # Рекурсивно вычисляем определитель
        determinant += sign * matrix[i][0] * calculate_determinant(minor)

    return determinant

