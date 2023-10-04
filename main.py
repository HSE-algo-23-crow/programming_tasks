import random

import numpy as np
import random as rnd


MATRIX = 'matrix'
DET = 'det'


def get_random_matrix_and_det(order):
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param order: порядок матрицы
    :raise Exception: если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: словарь с ключами matrix, det
    """
    if not isinstance(order, int) or order < 1:
        raise ValueError("Порядок должен быть натуральным числом")

    if order == 1:
        det = random.randint(1, 100)
        return {MATRIX: np.array([[det, ], ]), DET: det}

    n = np.zeros((order,order))
    for i in range(order):
        n[i,i] = 1
    for i in range(order * 10):
        firstindex = random.randint(0, order-1)
        secondindex = random.randint(0, order-1)
        while firstindex == secondindex:
            secondindex = random.randint(0, order-1)
        n[firstindex] += n[secondindex]
    det = random.randint(1, 100)
    n[0] *= det

    return {MATRIX:n, DET:det}

def main():
    n = 10
    print('Генерация матрицы порядка 10')
    gen_result = get_random_matrix_and_det(n)
    [print(row) for row in gen_result[MATRIX]]
    print('\nОпределитель сгенерированной матрицы равен', gen_result[DET])

    print('\nОпределитель, рассчитанный numpy, равен',
          round(np.linalg.det(np.array(gen_result[MATRIX]))))


if __name__ == '__main__':
    main()
