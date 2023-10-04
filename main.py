def calculate_determinant(matrix: [[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
def get_matrix_size() -> int:
    while True:
        try:
            size = int(input("Введите размер квадратной матрицы: ")) # Запрашиваем у пользователя размер матрицы
            if size <= 0: # Проверяем, что размер матрицы положительный
                raise ValueError
            return size
        except ValueError:
            print("Размер матрицы должен быть положительным целым числом") # Выводим сообщение об ошибке, если размер матрицы неверный

def get_matrix(size: int) -> [[int]]:
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            while True:
                try:
                    value = int(input(f"Введите элемент [{i}][{j}]: ")) # Запрашиваем у пользователя элемент матрицы
                    row.append(value)
                    break
                except ValueError:
                    print("Элемент матрицы должен быть целым числом") # Выводим сообщение об ошибке, если элемент матрицы неверный
        matrix.append(row)
    return matrix

def main():
    size = get_matrix_size() # Получаем размер матрицы от пользователя
    matrix = get_matrix(size) # Получаем матрицу от пользователя
    print("Матрица:")
    for row in matrix:
        print(row) # Выводим матрицу на экран
    try:
        determinant = calculate_determinant(matrix) # Вычисляем определитель матрицы
        print(f"Определитель матрицы: {determinant}") # Выводим определитель матрицы на экран
    except Exception as e:
        print(str(e)) # Выводим сообщение об ошибке, если матрица не является квадратной или содержит неверные значения элементов

def calculate_determinant(matrix: [[int]]) -> int:
    if matrix == None or matrix == []:
        raise Exception(
            "Вызвано исключение: в параметр передано значение None или пустой список")  # Проверяем, что матрица не является пустой
    if len(matrix) != len(matrix[0]):
        raise Exception(
            "Вызвано исключение: матрица не является квадратной")  # Проверяем, что матрица является квадратной
    for n in range(len(matrix)):
        if len(matrix[0]) != len(matrix[n]):
            raise Exception(
                "Вызвано исключение: строки матрицы содержат разное количество элементов")  # Проверяем, что все строки матрицы содержат одинаковое количество элементов
    n = len(matrix)
    match n:
        case 1:
            return matrix[0][0] # Если матрица имеет размер 1x1, то ее определитель равен единственному элементу
        case 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1] # Если матрица имеет размер 2x2, то ее определитель можно вычислить по формуле
        case n:
            summ = 0
            for a in range(n):
                minor = []
                for i in range(n):
                    minor2 = []
                    for j in range(n):
                        if i != 0 and j != a:
                            minor2 += [matrix[i][j]]
                    if minor2 != []:
                        minor += [minor2]
                summ += matrix[0][a]*calculate_determinant(minor)*(-1)**a # Если матрица имеет размер больше 2x2, то ее определитель можно вычислить рекурсивно
            return summ

if __name__ == '__main__':
    main()


def main():
    matrix = [[1, 2],
              [3, 4]]
    print('Матрица')
    for row in matrix:
        print(row)

    print(f'Определитель матрицы равен {calculate_determinant(matrix)}')


if __name__ == '__main__':
    main()
