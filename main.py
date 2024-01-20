INF = float('inf')
COST = 'cost'
PATH = 'path'
PARAM_ERR_MSG = ('Таблица цен не является прямоугольной матрицей с '
                 'числовыми значениями')


def get_min_cost_path(price_table: list[list[float | int]]) -> \
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

    if (price_table is None or len(price_table) == 0):
        raise ValueError(PARAM_ERR_MSG)
    row_len = len(price_table[0])
    if (row_len == 0):
        raise ValueError(PARAM_ERR_MSG)
    for row in price_table:
        if (len(row) != row_len):
            raise ValueError(PARAM_ERR_MSG)
        for value in row:
            if not (type(value) is int or type(value) is float):
                raise ValueError(PARAM_ERR_MSG)

    min_cost_table = get_min_cost_table([[y for y in x] for x in price_table])
    cost = min_cost_table[len(min_cost_table) - 1][len(min_cost_table[len(min_cost_table) - 1]) - 1]
    path = get_path_recursive(min_cost_table, price_table)
    return {
        COST: cost,
        PATH: path
    }


def get_path_recursive(min_cost_table, price_table):
    path = []
    current_index = (len(price_table) - 1, len(price_table[len(price_table) - 1]) - 1)
    path.append(current_index)
    current_cost = min_cost_table[current_index[0]][current_index[1]]
    while current_index[0] != 0 or current_index[1] != 0:
        right_cost = min_cost_table[current_index[0]][current_index[1] - 1]
        top_cost = min_cost_table[current_index[0] - 1][current_index[1]]
        if (current_index[0] == 0) or (round(current_cost - right_cost,1) == price_table[current_index[0]][current_index[1]]):
            path.append((current_index[0], current_index[1] - 1))
            current_cost = right_cost
            current_index = (current_index[0], current_index[1] - 1)
        elif (current_index[1] == 0) or (round(current_cost - top_cost,1) == price_table[current_index[0]][current_index[1]]):
            path.append((current_index[0] - 1, current_index[1]))
            current_cost = top_cost
            current_index = (current_index[0] - 1, current_index[1])
    return [x for x in reversed(path)]


def get_min_cost_table(price_table):
    for i in range(len(price_table)):
        for j in range(len(price_table[i])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                price_table[i][j] += price_table[i][j - 1]
            elif j == 0:
                price_table[i][j] += price_table[i - 1][j]
            else:
                price_table[i][j] += min(price_table[i - 1][j], price_table[i][j - 1])

    return price_table


def main():
    # table = [[1, 2, 2],
    #          [3, 4, 2],
    #          [1, 1, 2]]
    table = [[1, 2, 2],
             [3, 4, 1]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
