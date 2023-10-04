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

def det(arr):
    if (len(arr) == 1) & (len(arr[0]) == 1):
        return arr[0][0]
    else:
        res = 0
        for k in range(len(arr[0])):
            arr_new = resize(arr, k)
            res += ((-1)*k)*arr[0][k]*det(arr_new)
        return res

def get_random_matrix_and_det(n):
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param n: порядок матрицы
    :raise Exception: если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: словарь с ключами matrix, det
    """
    a = []
    m = n
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(round(random.uniform(-10, 10), 3))
    determinant = det(a)
    matrixDict = {a:determinant}
    return matrixDict


def main():
    n = 10
    print('Генерация матрицы порядка 10')
    gen_result = get_random_matrix_and_det(n)
    # for key in gen_result.items():
    #     print(f"Key: {key}")
    [print(row) for row in gen_result[MATRIX]]
    print('\nОпределитель сгенерированной матрицы равен', gen_result[DET])

    print('\nОпределитель, рассчитанный numpy, равен',
          round(np.linalg.det(np.array(gen_result[MATRIX]))))


if __name__ == '__main__':
    main()
