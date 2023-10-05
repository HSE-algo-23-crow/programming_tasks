import random

import numpy as np
import random as rnd

MATRIX = 'matrix'
DET = 'det'


def get_random_matrix_and_det(order):
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя. Благодаря алгебраическим свойствам матрицы, мы можем использовать
    сложение случайных строк данной квадратной матрицы для получения случайных значений
    элементов без изменения определителя матрицы. Домножение первой строки матрицы на необходимое значение определителя
    позволяет получить матрицу с рандомными значениями матрицы и необходимым определителем.
    :param order: Порядок матрицы
    :raise Exception: Если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: Словарь с ключами matrix, det
    """
    if type(order) != int or order < 1:
        raise ValueError("Порядок должен быть натуральным целочисленным числом!")

    if order == 1:
        det = random.randint(1, 100)
        matrix = np.array([[det, ], ])
        return {MATRIX: matrix, DET: det}

    matrix = np.zeros((order, order))

    for i in range(order):
        matrix[i, i] = 1  # Получение единичной матрицы

    for i in range(order * rnd.randint(3, 8)):
        row_indx = random.randint(0, order - 1)
        col_indx = random.randint(0, order - 1)  # Получение случайных индексов строк матрицы для их сложения

        while row_indx == col_indx:
            col_indx = random.randint(0, order - 1) # Исключение сложения строки с собой же

        matrix[row_indx] += matrix[col_indx] * rnd.randint(1, 5)

    det = rnd.randint(1, 10)
    matrix[0] *= det

    return {MATRIX: matrix, DET: det}


def main():
    n = 3
    print('Генерация матрицы порядка 3')
    gen_result = get_random_matrix_and_det(n)
    [print(row) for row in gen_result[MATRIX]]
    print('\nОпределитель сгенерированной матрицы равен', gen_result[DET])

    print('\nОпределитель, рассчитанный numpy, равен',
          round(np.linalg.det(np.array(gen_result[MATRIX]))))


if __name__ == '__main__':
    main()
