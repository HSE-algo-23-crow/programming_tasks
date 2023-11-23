import numpy as np # Используем библиотеку NumPy для генерации случайной матрицы и вычисления определителя

def get_random_matrix_and_det(size, determinant):
    # Генерируем случайную матрицу с целочисленными значениями
    matrix = np.random.randint(low=-10, high=10, size=(size, size))

    # Пересчитываем определитель с использованием библиотеки NumPy
    current_det = int(round(np.linalg.det(matrix)))

    # Повторяем генерацию матрицы, пока не достигнем нужного значения определителя
    while current_det != determinant:
        matrix = np.random.randint(low=-10, high=10, size=(size, size))
        current_det = int(round(np.linalg.det(matrix)))

    return matrix

# Пример использования:
size = 3  # Размер матрицы (3x3)
desired_determinant = 42  # Заданное значение определителя

random_matrix = get_random_matrix_and_det(size, desired_determinant)
print("Случайная матрица:")
print(random_matrix)
print("Определитель матрицы:", np.linalg.det(random_matrix))
