PARAM_ERR_MSG = 'Таблица не является прямоугольной матрицей со значениями 0 1'


def get_path_count(allow_table: list[list[int]]) -> int:
    """Возвращает количество допустимых путей в таблице из правого верхнего угла
    в левый нижний.
    Каждая ячейка в таблице содержит 1 если ее посещение возможно и 0 если
    не возможно.
    Перемещение из ячейки в ячейку можно производить только по горизонтали
    вправо или по вертикали вниз.
    :param allow_table: Таблица с признаком возможности посещения ячеек.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей
    со значениями 0 1.
    :return: количество путей.
    """
    if not allow_table or not all(isinstance(row, list) and row for row in allow_table):
        raise ValueError(PARAM_ERR_MSG)

    row_cnt = len(allow_table)
    col_cnt = len(allow_table[0])

    # Проверяем, является ли матрица прямоугольной и содержит ли только 0 или 1
    if any(len(row) != col_cnt for row in allow_table) or any(
            cell not in [0, 1] for row in allow_table for cell in row):
        raise ValueError(PARAM_ERR_MSG)

    # Создаем таблицу для хранения количества путей
    path_cnt_tbl = [[0] * col_cnt for _ in range(row_cnt)]

    # Инициализируем первую ячейку
    path_cnt_tbl[0][0] = allow_table[0][0]

    # Заполняем таблицу количеством путей
    for i in range(row_cnt):
        for j in range(col_cnt):
            if allow_table[i][j] == 0:
                path_cnt_tbl[i][j] = 0
            else:
                if i > 0:
                    path_cnt_tbl[i][j] += path_cnt_tbl[i - 1][j]
                if j > 0:
                    path_cnt_tbl[i][j] += path_cnt_tbl[i][j - 1]

    # Возвращаем количество путей к правой нижней ячейке
    return path_cnt_tbl[-1][-1]

def main():
    table = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
    print(get_path_count(table))


if __name__ == '__main__':
    main()
