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
    test_input(price_table)

    new_table = [[0 for j in range(len(price_table[i]))] for i in range(len(price_table))]
    path_table = [[-1 for j in range(len(price_table[i]))] for i in range(len(price_table))]

    new_table[0][0] = price_table[0][0]

    for i in range(1, len(price_table)):
        if price_table[i][0] is None:
            for j in range(i, len(price_table)):
                new_table[j][0] = None
            break
        else:
            new_table[i][0] = new_table[i-1][0] + price_table[i][0]
            path_table[i][0] = 0

    for i in range(1, len(price_table[0])):
        if price_table[0][i] is None:
            for j in range(i, len(price_table[0])):
                new_table[0][j] = None
            break
        else:
            new_table[0][i] = new_table[0][i-1] + price_table[0][i]
            path_table[0][i] = 1

    for i in range(1, len(price_table)):
        for j in range(1, len(price_table[i])):
            if price_table[i][j] is None:
                new_table[i][j] = None
            else:
                if new_table[i-1][j] is None and new_table[i][j-1] is None:
                    new_table[i][j] = None
                elif new_table[i-1][j] is None:
                    new_table[i][j] = new_table[i][j-1] + price_table[i][j]
                    path_table[i][j] = 1
                elif new_table[i][j-1] is None:
                    new_table[i][j] = new_table[i-1][j] + price_table[i][j]
                    path_table[i][j] = 0
                else:
                    if new_table[i-1][j] < new_table[i][j-1]:
                        new_table[i][j] = new_table[i-1][j] + price_table[i][j]
                        path_table[i][j] = 0
                    else:
                        new_table[i][j] = new_table[i][j-1] + price_table[i][j]
                        path_table[i][j] = 1

    if new_table[-1][-1] is None:
        return {COST: None, PATH: None}
    else:
        path = [(len(price_table)-1, len(price_table[0])-1)]
        i = len(price_table)-1
        j = len(price_table[0])-1
        while i != 0 or j != 0:
            if path_table[i][j] == 0:
                path.append((i-1, j))
                i -= 1
            else:
                path.append((i, j-1))
                j -= 1

        for it in range(i, 0, -1):
            path.append((it-1, 0))
        for jt in range(j, 0, -1):
            path.append((0, jt-1))
        path.reverse()
        return {COST: new_table[-1][-1], PATH: path}


def test_input(price_table):
    if type(price_table) != list:
        raise ValueError(PARAM_ERR_MSG)
    if len(price_table) == 0 or len(price_table[0]) == 0:
        raise ValueError(PARAM_ERR_MSG)
    if any(map(lambda rows: any(map(lambda elem: not (type(elem) in [int, float] or elem is None), rows)), price_table)):
        raise ValueError(PARAM_ERR_MSG)
    row_lens = map(len, price_table)
    row_lens = list(row_lens)
    first_len = row_lens[0]
    if any(map(lambda x: x != first_len, row_lens)):
        raise ValueError(PARAM_ERR_MSG)



def main():
    table = [[1, 2, 2],
             [3, None, 2],
             [None, 2, 2]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
