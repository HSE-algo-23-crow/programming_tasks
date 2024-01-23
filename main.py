INF = float('inf')
COST = 'cost'
PATH = 'path'
PARAM_ERR_MSG = ('Таблица цен не является прямоугольной матрицей с '
                 'числовыми значениями')

def get_min_cost_path(price_table: list[list[float or int]]) -> \
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
    validate_params_raises_ex(price_table)
    cost_tbl = __get_cost_tbl(price_table)
    path_back = __get_path_back(cost_tbl)
    return {COST: cost_tbl[-1][-1], PATH: path_back[::-1]}


def __get_path_back(cost_tbl):
    cur_row = len(cost_tbl) - 1
    cur_col = len(cost_tbl[0]) - 1
    path_back = [(cur_row - 1, cur_col - 1)]
    while cur_row > 1 or cur_col > 1:
        cost_up = cost_tbl[cur_row - 1][cur_col]
        cost_left = cost_tbl[cur_row][cur_col - 1]
        if cost_up <= cost_left:
            cur_row -= 1
        else:
            cur_col -= 1
        path_back.append((cur_row - 1, cur_col - 1))
    return path_back


def __get_cost_tbl(price_table):
    row_cnt = len(price_table) + 1
    col_cnt = len(price_table[0]) + 1
    path_cnt_tbl = [[INF] * col_cnt for _ in range(row_cnt)]
    path_cnt_tbl[1][1] = price_table[0][0]
    for row_idx in range(1, row_cnt):
        for col_idx in range(1, col_cnt):
            if row_idx == col_idx == 1:
                continue
            cost_up = path_cnt_tbl[row_idx - 1][col_idx]
            cost_left = path_cnt_tbl[row_idx][col_idx - 1]
            path_cnt_tbl[row_idx][col_idx] = min(cost_up, cost_left) + price_table[row_idx - 1][col_idx - 1]
    return path_cnt_tbl


def validate_params_raises_ex(price_table):
    if price_table is None or len(price_table) == 0 or len(price_table[0]) == 0:
        raise ValueError(PARAM_ERR_MSG)
    for row in price_table:
        if not all(isinstance(this_cost, (int, float)) for this_cost in row):
            raise ValueError(PARAM_ERR_MSG)
    col_cnt = len(price_table[0])
    for row in price_table:
        if len(row) != col_cnt:
            raise ValueError(PARAM_ERR_MSG)

def main():
    table = [[1, 2, 2],
             [3, 4, 2],
             [1, 1, 2]]
    print(get_min_cost_path(table))

if __name__ == 'main':
    main()