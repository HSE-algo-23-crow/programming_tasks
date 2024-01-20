INF = float('inf')
COST = 'cost'
PATH = 'path'
PARAM_ERR_MSG = ('Таблица цен не является прямоугольной матрицей с '
                 'числовыми значениями')


def get_min_cost_path(price_table: list[list[float | int | None]]) ->\
        dict[str: float | None, str: list[tuple[int, int]] | None]:
    """Возвращает путь минимальной стоимости в таблице из правого верхнего угла
    в левый нижний.
    Каждая ячейка в таблице имеет цену посещения.
    Некоторые ячейки запрещены к посещению, вместо цены посещения значение None.
    Перемещение из ячейки в ячейку можно производить только по горизонтали
    вправо или по вертикали вниз.
    :param price_table: Таблица с ценой посещения для каждой ячейки.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей с
    числовыми значениями.
    :return: Словарь с ключами:
    cost - стоимость минимального пути или None если пути не существует,
    path - путь, список кортежей с индексами ячеек, или None если пути
    не существует.
    """
    validate_table_raises_ex(price_table)
    if (price_table[0][0] is None) or (price_table[-1][-1] is None):
        return {COST: None, PATH: None}
    change_none_to_inf(price_table)
    cost_table = get_cost_table(price_table[:])
    path_back = get_path_back(cost_table)
    if path_back is None:
        return {COST: None, PATH: None}
    return {COST: cost_table[-1][-1], PATH: path_back[::-1]}

def get_cost_table(price_table: list[list[float | int | None ]]):
    row_count = len(price_table) + 1
    col_count = len(price_table[0]) + 1
    path_count_tbl = [[INF] * col_count for _ in range(row_count)]
    path_count_tbl[1][1] = price_table[0][0]
    for row_index in range(1, row_count):
        for col_index in range(1, col_count):
            if (row_index == col_index == 1):
                continue
            cost_up = path_count_tbl[row_index - 1][col_index]
            cost_left = path_count_tbl[row_index][col_index - 1]
            path_count_tbl[row_index][col_index] = min(cost_up, cost_left) + price_table[row_index - 1][col_index - 1]
    return path_count_tbl

def get_path_back(cost_table: list[list[int | float | None]]):
    cur_row = len(cost_table)-1
    cur_col = len(cost_table[0])-1
    path_back = [(cur_row-1, cur_col-1)]
    while cur_row != 1 or cur_col != 1:
        cost_up = cost_table[cur_row-1][cur_col]
        cost_left = cost_table[cur_row][cur_col-1]
        if cost_up == INF and cost_left == INF:
            return None
        if cost_up <= cost_left:
            cur_row -= 1
        else:
            cur_col -= 1
        path_back.append((cur_row-1, cur_col-1))
    return path_back

def change_none_to_inf(price_table: list[list[float | int| None ]]):
    for row_index in range(len(price_table)):
        for column_index in range(len(price_table[0])):
            if price_table[row_index][column_index] is None:
                price_table[row_index][column_index] = INF



def validate_table_raises_ex(price_table: list[list[float | int | None]]) -> None:
    if type(price_table) is list:
        if len(price_table) == 0:
            raise ValueError(PARAM_ERR_MSG)

        if type(price_table[0]) is list:
            if len(price_table[0]) == 0:
                raise ValueError(PARAM_ERR_MSG)

            max_length = max([len(row) for row in price_table])
            for row_index in range(len(price_table)):

                if len(price_table[row_index]) != max_length:
                    raise ValueError(PARAM_ERR_MSG)

                for column_index in range(len(price_table[row_index])):

                    if not check_data_type(price_table[row_index][column_index]):
                        raise ValueError(PARAM_ERR_MSG)
    else:
        raise ValueError(PARAM_ERR_MSG)


def check_data_type(data):
    """
    Проверяет является ли переменная нужного типа (float, int, None)
    :param data: Переменная, которую стоит проверить
    :return: true или false в зависимости от типа переменной
    """
    return isinstance(data, float) or isinstance(data, int) or data is None


def ad():
    pass

def main():
    table = [[1, 2, 2],
             [3, None, 2],
             [None, 1, 2]]
    table_copy = table[:]
    for row_index in range(len(table_copy)):
        table_copy[row_index] = table[row_index][:]
    print(get_min_cost_path(table_copy))


if __name__ == '__main__':
    main()
