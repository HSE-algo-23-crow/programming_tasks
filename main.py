from __future__ import annotations

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
    __check_value_validation(price_table)
    return __get_path_cnt_tbl(price_table)


def __check_value_validation(price_table):
    if price_table == None or price_table == [[]] or price_table == []:
        raise ValueError(PARAM_ERR_MSG)
    for sublist in price_table:
        for item in sublist:
            if not isinstance(item,float) and not isinstance(item,int) and not item is None:
                raise ValueError(PARAM_ERR_MSG)
    length = len(price_table[0])
    for sublist in price_table:
        if not length == len(sublist):
            raise ValueError(PARAM_ERR_MSG)
        length = len(sublist)
def __get_path_cnt_tbl(allow_table):
    row_cnt = len(allow_table) + 1
    col_cnt = len(allow_table[0]) + 1
    cost_cnt_tbl = [[INF]*col_cnt for _ in range(row_cnt)] # заполняем новую таблицу INF
    cost_cnt_tbl[1][1] = allow_table[0][0] # переносим первый начало из заданной таблицы
    for row_indx in range(1, row_cnt):
        for col_indx in range(1, col_cnt):
            if row_indx == 1 and col_indx == 1:
                continue
            cnt_up = cost_cnt_tbl[row_indx-1][col_indx]
            cnt_left = cost_cnt_tbl[row_indx][col_indx-1]
            cnt_current = allow_table[row_indx - 1][col_indx -1]
            if cnt_current == None:
                cnt_current = INF
            cost_cnt_tbl[row_indx][col_indx] = min(cnt_up, cnt_left) + cnt_current
    if cost_cnt_tbl[-1][-1] == INF or cost_cnt_tbl[-1][-1] is None:
        return {COST: None, PATH: None}
    path = __find_path(cost_cnt_tbl)
    return {COST: cost_cnt_tbl[-1][-1], PATH: path}
def __find_path(cost_cnt_tbl):
    path = []
    row_indx, col_indx = len(cost_cnt_tbl) - 1, len(cost_cnt_tbl[0]) - 1
    while row_indx > 0 and col_indx > 0:
        path.append((row_indx - 1, col_indx - 1))
        if row_indx == 0:
            col_indx -= 1
        elif col_indx == 0:
            row_indx -= 1
        else:
            if cost_cnt_tbl[row_indx-1][col_indx] < cost_cnt_tbl[row_indx][col_indx-1]:
                row_indx -= 1
            else:
                col_indx -= 1
    path.reverse()
    return path
def main():
    table = [[None]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
