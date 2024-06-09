from permutations import generate_permutations


NullableNumber = int | float | None

INFINITY = float('inf')
DISTANCE = 'distance'
PATH = 'path'
PARAM_ERR_MSG = ('Таблица расстояний не является прямоугольной матрицей с '
                 'числовыми значениями')
NEG_VALUE_ERR_MSG = 'Расстояние не может быть отрицательным'

def matrix_validation(dist_matrix: list[list[NullableNumber]]):
    if not isinstance(dist_matrix, list):
        raise TypeError(PARAM_ERR_MSG)
    elif not dist_matrix or len(dist_matrix) != len(dist_matrix[0]):
        raise TypeError(PARAM_ERR_MSG)
    else:
        for i in range(len(dist_matrix)):
            if not isinstance(dist_matrix[i], list) or len(dist_matrix[0]) != len(dist_matrix[i]):
                raise TypeError(PARAM_ERR_MSG.format(dist_matrix[i]))
            for j in range(len(dist_matrix[i])):
                if isinstance(dist_matrix[i][j],str):
                    raise TypeError(PARAM_ERR_MSG)
                elif isinstance(dist_matrix[i][j], (int, float)) and dist_matrix[i][j] < 0:
                    raise ValueError(NEG_VALUE_ERR_MSG)

def is_path_possible(distance_matrix):
    def dfs(city, visited):
        visited.add(city)
        for next_city in range(len(distance_matrix)):
            if distance_matrix[city][next_city] is not None and next_city not in visited:
                dfs(next_city, visited)

    for i in range(len(distance_matrix)):
        visited = set()
        dfs(i, visited)
        if len(visited) != len(distance_matrix):
            return False
    return True

def generate_permutations(lst):
    # Если список пуст, возвращаем пустой список
    if len(lst) == 0:
        return []
    # Если в списке один элемент, возвращаем список с этим элементом
    if len(lst) == 1:
        return [lst]
    # Список для хранения всех перестановок
    permutations = []
    # Проходим по всем элементам списка
    for i in range(len(lst)):
        m = lst[i]
        # Получаем список без текущего элемента
        remLst = lst[:i] + lst[i+1:]
        # Для каждой перестановки оставшегося списка
        for p in generate_permutations(remLst):
            # Добавляем текущий элемент к перестановке
            permutations.append([m] + p)
    return permutations

def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    number_of_cities = len(distance_matrix)
    if len(route) == 1:
        return 0
    for i in range(number_of_cities):
        # Суммируем расстояние от текущего города до следующего
        if distance_matrix[route[i]][route[(i + 1) % number_of_cities]] is not None:
            total_distance += distance_matrix[route[i]][route[(i + 1) % number_of_cities]]
        else:
            total_distance += INFINITY
    return total_distance

def get_salesman_path(dist_matrix: list[list[NullableNumber]]) -> \
        dict[str, float | list[int]]:
    """Решает задачу коммивояжёра с использованием полного перебора.

    :param dist_matrix: Матрица расстояний.
    :raise TypeError: Если таблица расстояний не является прямоугольной
    матрицей с числовыми значениями.
    :raise ValueError: Если в матрице присутствует отрицательное значение.
    :return: Словарь с ключами: distance - кратчайшее расстояние,
    path - список с индексами вершин на кратчайшем маршруте.
    """
    matrix_validation(dist_matrix)

    if not is_path_possible(dist_matrix):
        return {'distance': None, 'path': []}
    else:
        cities = list(range(len(dist_matrix)))
        shortest_route = None
        min_distance = float('inf')

        for route in generate_permutations(cities):
            current_distance = calculate_total_distance(route, dist_matrix)
            # Если расстояние меньше текущего минимального
            if current_distance < min_distance:
                # Обновляем минимальное расстояние и лучший маршрут
                min_distance = current_distance
                if len(dist_matrix) > 1:
                    route.append(route[0])
                shortest_route = route
            # Возвращаем лучший маршрут и его расстояние
    return {DISTANCE: min_distance, PATH: shortest_route}

if __name__ == '__main__':
    print('Пример решения задачи коммивояжёра\n\nМатрица расстояний:')
    matrix = [[None]]

    for row in matrix:
        print(row)

    print('\nРешение задачи:')
    print(get_salesman_path(matrix))
