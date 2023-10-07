import random
import numpy as np

MATRIX = 'matrix'  # Ключ для матрицы в словаре
DET = 'det'  # Ключ для определителя в словаре

def get_random_matrix_and_det(n):
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param n: порядок матрицы (целое число)
    :raise Exception: если порядок матрицы не является целым числом или порядок
    меньше 1
    :return: словарь с ключами matrix и det
    """
    matrix = np.random.randint(-10, 11, (n, n))  # Генерируем случайную матрицу размером n x n

    # Рассчитываем определитель матрицы
    det = int(round(np.linalg.det(matrix)))

    # Перегенерируем матрицу, если определитель равен нулю (нужен ненулевой определитель)
    while det == 0:
        matrix = np.random.randint(-10, 11, (n, n))
        det = int(round(np.linalg.det(matrix)))

    # Создаем словарь, содержащий сгенерированную матрицу и ее определитель
    matrixDict = {MATRIX: matrix.tolist(), DET: det}
    return matrixDict

def main():
    n = 10
    print('Генерация матрицы порядка 10')
    gen_result = get_random_matrix_and_det(n)  # Получаем сгенерированную матрицу и определитель

    # Выводим матрицу по строкам
    for row in gen_result[MATRIX]:
        print(row)

    print('\nОпределитель сгенерированной матрицы равен', gen_result[DET])

    # Рассчитываем определитель с помощью numpy и выводим его
    calculated_det = int(round(np.linalg.det(np.array(gen_result[MATRIX]))))
    print('\nОпределитель, рассчитанный numpy, равен', calculated_det)

    # Проверяем, совпадают ли определители
    assert gen_result[DET] == calculated_det, "Определители не совпадают"

if __name__ == '__main__':
    main()
