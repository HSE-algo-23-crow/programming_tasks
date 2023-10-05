import random

import numpy as np
import random as rnd


MATRIX = 'matrix'
DET = 'det'

def resize(arr, s_num):
    result_arr = arr[1:]
    for j in range(len(result_arr)):
        result_arr[j] = result_arr[j][:s_num] + result_arr[j][s_num + 1:]
    return result_arr

def detFun(arr):
    if (len(arr) == 1) & (len(arr[0]) == 1):
        return arr[0][0]
    else:
        res = 0
        for k in range(len(arr[0])):
            arr_new = resize(arr, k)
            res += ((-1)**k)*arr[0][k]*detFun(arr_new)
        return res

def get_random_matrix_and_det(n):
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param n: порядок матрицы
    :raise Exception: если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: словарь с ключами matrix, det
    """
    matrix = []
    m = n
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(round(random.uniform(-10, 10), 3))
    det = round(detFun(matrix))
    for i in range(n):
        matrix[i] = (*matrix[i],)

    matrix = (*matrix,)
    matrixDict = {MATRIX: matrix, DET: det}
    return matrixDict


def main():
    n = 10
    print('Генерация матрицы порядка 10')
    gen_result = get_random_matrix_and_det(n)
    # MATRIX = gen_result.keys()
    [print(row) for row in gen_result[MATRIX]]
    print('\nОпределитель сгенерированной матрицы равен', gen_result[DET])

    print('\nОпределитель, рассчитанный numpy, равен',
          round(np.linalg.det(np.array(gen_result[MATRIX]))))


if __name__ == '__main__':
    main()