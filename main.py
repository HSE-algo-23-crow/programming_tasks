PARAM_ERR_MSG = 'Таблица не является прямоугольной матрицей со значениями 0 1'


def get_path_count_recursive(allow_table: list[list[int]], row: int, col: int) -> int:
    """Рекурсивно возвращает количество допустимых путей из ячейки (row,col)
    в правый нижний угол таблицы.
    """
    # Проверка на выход за границы таблицы
    if row >= len(allow_table) or col >= len(allow_table[0]) or allow_table[row][col] == 0:
        return 0

    # Если достигнут правый нижний угол, возвращаем 1, т.к. достигнут один путь
    if row == len(allow_table) - 1 and col == len(allow_table[0]) - 1:
        return 1

    # Рекурсивно двигаемся вправо и вниз, суммируя количество путей
    return get_path_count_recursive(allow_table, row, col + 1) + get_path_count_recursive(allow_table, row + 1, col)


def get_path_count(allow_table: list[list[int]]) -> int:
    """Возвращает количество допустимых путей в таблице из правого верхнего угла
    в левый нижний, используя рекурсию.
    :param allow_table: Таблица с признаком возможности посещения ячеек.
    :raise ValueError: Если таблица не является прямоугольной матрицей
    со значениями 0 1.
    :return: количество путей.
    """
    # Проверка, является ли таблица правильной прямоугольной матрицей со значениями 0 или 1
    if allow_table == None or allow_table == [] or any(row == [] or len(row) != len(allow_table[0]) or any(not(isinstance(val, int)) or val not in {0, 1} for val in row) for row in allow_table):
        raise ValueError(PARAM_ERR_MSG)

    return get_path_count_recursive(allow_table, 0, 0)


def main():
    table = [[1, 1],
                 [1, []]]
    try:
        print(get_path_count(table))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()