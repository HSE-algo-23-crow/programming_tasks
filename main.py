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
    pass


def validate_table_raises_ex(price_table: list[list[float | int | None]]) -> None:
    if price_table is not list[list[float | int | None]]:
        raise ValueError(PARAM_ERR_MSG)
    if len(price_table) != len(price_table[0]):
        for row_index in range(len(price_table)):
            for column_index in range(len(price_table[row_index])):
                pass
def ad():
    pass

def main():
    table = [[1, 2, 2],
             [3, None, 2],
             [None, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
