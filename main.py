INF = float('inf')
COST = 'cost'
PATH = 'path'
PARAM_ERR_MSG = ('Таблица цен не является прямоугольной матрицей с '
                 'числовыми значениями')


def get_min_cost_path(price_table: list[list[float | int]]) ->\
        dict[str: float, str: list[tuple[int, int]]]:
    """Возвращает путь минимальной стоимости в таблице из правого верхнего угла
    в левый нижний.
    Каждая ячейка в таблице имеет цену посещения.
    Перемещение из ячейки в ячейку можно производить только по горизонтали
    вправо или по вертикали вниз.
    :param price_table: Таблица с ценой посещения для каждой ячейки.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей с
    числовыми значениями.
    :return: Словарь с ключами:
    cost - стоимость минимального пути,
    path - путь, список кортежей с индексами ячеек.
    """
    __validate_params_raises_ex(price_table)
    cost_tbl = __get_cost_tbl(price_table)
    path_back = __get_path_back(cost_tbl)
    return {COST: cost_tbl[-1][-1], PATH: path_back[::-1]}


def __validate_params_raises_ex(price_table):
    """Валидация входных данных (price_table и её элементов)
    :param price_table: Данная таблица стоимости путей
    :raise ValueError: Выброс исключения при невыполнении условия, что матрица - прямоугольная с числовыми значениями
    """

    if price_table is None:
        raise ValueError(PARAM_ERR_MSG)

    if not len(price_table):
        raise ValueError(PARAM_ERR_MSG)

    if any([len(x) == 0 for x in price_table]):
        raise ValueError(PARAM_ERR_MSG)

    first_row_len = len(price_table[0])
    for row in price_table:
        # Проверка на то, что в матрице нет строк разной длины
        if len(row) != first_row_len:
            raise ValueError(PARAM_ERR_MSG)
        for item in row:
            # Проверка на то, что элементы матрицы соответствуют только типам int и float
            if not isinstance(item, int) and not isinstance(item, float):
                raise ValueError(PARAM_ERR_MSG)


def __get_path_back(cost_tbl):
    cur_row = len(cost_tbl) - 1
    cur_col = len(cost_tbl[0]) - 1
    path_back = []
    while cur_row and cur_col:
        path_back.append((cur_row - 1, cur_col - 1))
        cost_up = cost_tbl[cur_row - 1][cur_col]
        cost_left = cost_tbl[cur_row][cur_col - 1]
        if cost_up <= cost_left:
            cur_row -= 1
        else:
            cur_col -= 1
    return path_back


def __get_cost_tbl(price_table):
    row_cnt = len(price_table) + 1
    col_cnt = len(price_table[0]) + 1
    cost_tbl = [[INF]*col_cnt for _ in range(row_cnt)]
    cost_tbl[1][1] = price_table[0][0]
    for row_idx in range(1, row_cnt):
        for col_idx in range(1, col_cnt):
            if row_idx == col_idx == 1:
                continue
            cost_up = cost_tbl[row_idx - 1][col_idx]
            cost_left = cost_tbl[row_idx][col_idx - 1]
            cost_tbl[row_idx][col_idx] = price_table[row_idx - 1][col_idx - 1] + min(cost_up, cost_left)
    return cost_tbl


def main():
    table = [[1, 2, 2],
             [3, 4, 2],
             [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
