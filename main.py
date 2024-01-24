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

    err = is_error(allow_table)
    if (err): return err
    return get_path_count_table(allow_table)


def is_error(price_table):
    # 1) табица не None 2) табица не пустая 3) первая строка табицы не пустая
    if price_table == None or len(price_table) == 0 or len(price_table[0]) == 0: raise ValueError(PARAM_ERR_MSG)

    for row in price_table:
        # у всех строк одинаковая длина
        if len(row) != len(price_table[0]): raise ValueError(PARAM_ERR_MSG)
        for item in row:
            # число либо 0, либо 1
            if item not in [0, 1]: raise ValueError(PARAM_ERR_MSG)


def get_path_count_table(price_table):
    paths_table = [[0] * len(price_table[0]) for _ in range(len(price_table))]
    # вставляем левый верхний элемент в копию таблицы
    paths_table[0][0] = price_table[0][0]

    for i in range(len(paths_table)):
        for j in range(len(paths_table[0])):
            # иначе остаётся нолик и мы ничего не делаем
            if price_table[i][j] != 0:
                # для ненулевых элментов добавляем то элементы сверху или слева
                if i > 0: paths_table[i][j] += paths_table[i - 1][j]
                if j > 0: paths_table[i][j] += paths_table[i][j - 1]

    # возвращаем последний элемент копии таблицы
    return paths_table[-1][-1]


def main():
    table = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
    print(get_path_count(table))


if __name__ == '__main__':
    main()