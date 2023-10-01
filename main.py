import random

import numpy as np
import random as rnd


MATRIX = 'matrix'
DET = 'det'


def get_random_matrix_and_det(order) -> {}:
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param order: порядок матрицы
    :raise Exception: если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: словарь с ключами matrix, det
    """

    validate_order_raises_exception(order)
    return create_random_matrix(order)


def create_random_matrix(order) -> {}:
    """
    Функция, которая создаёт "случайную матрицу"
    :param order: порядок целочисленной квадратной матрицы
    :return: возвращает словарь с матрицей и её определителем
    """
    matrix_and_det = {'matrix': [], 'det': 1}

    for row_index in range(0, order):
        matrix_row = []

        for column_index in range(0, order):
            if column_index < row_index:
                matrix_row.append(0)
            else:
                matrix_row.append(rnd.randint(-10, 10))

            if column_index == row_index:
                matrix_and_det['det'] *= matrix_row[column_index]

        matrix_and_det['matrix'].append(matrix_row)

    for row_index in range(1, order):
        k = random.randint(2, 5)
        for column_index in range(0, order):
            matrix_and_det['matrix'][row_index][column_index] += matrix_and_det['matrix'][row_index-1][column_index]*k
    return matrix_and_det


def validate_order_raises_exception(order):
    """
    Функция, которая проверяет валидность введённых данных
    :param order: порядок целочисленной квадратной матрицы
    :raise Exception: если порядок матрицы неверного типа или меньше единицы
    """
    if type(order) != int:
        raise TypeError("Неверный тип данных для введённого значения порядка!")
    elif order < 1:
        raise ValueError("Порядок матрицы не может быть меньше единицы!")


def main():
    """
    Основное тело программы
    :return:
    """
    n = 10
    print('Генерация матрицы порядка 10')
    matrix_and_det = get_random_matrix_and_det(n)
    [print(row) for row in matrix_and_det[MATRIX]]
    print('\nОпределитель сгенерированной матрицы равен', matrix_and_det[DET])

    print('\nОпределитель, рассчитанный numpy, равен',
          round(np.linalg.det(np.array(matrix_and_det['matrix']))))


if __name__ == '__main__':
    main()
