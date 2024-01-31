PROFIT = 'profit'
DISTRIBUTION = 'distribution'
PARAM_ERR_MSG = ('Таблица прибыли от проектов не является прямоугольной '
                 'матрицей с числовыми значениями')
NEG_PROFIT_ERR_MSG = 'Значение прибыли не может быть отрицательно'
DECR_PROFIT_ERR_MSG = 'Значение прибыли не может убывать с ростом инвестиций'


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def get_invest_distribution(profit_matrix: list[list[int]]) -> \
        dict[str: int, str: list[int]]:
    """Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами. Инвестиции распределяются кратными частями.
    :param profit_matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций. Проекты указаны в столбцах, уровни
    инвестиций в строках.
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    :return: Словарь с ключами:
    profit - максимально возможная прибыль от инвестиций,
    distribution - распределение инвестиций между проектами.
    """

    is_error(profit_matrix)

    profit_matrix_copy = profit_matrix.copy()
    path_matrix = []
    for j in range(len(profit_matrix[0]) - 1):
        matrix = [[0, 0]]
        for i in range(len(profit_matrix)):
            matrix.append([profit_matrix_copy[i][j],
                          profit_matrix_copy[i][j+1]])

        s_max = 0
        path = [""] * (len(matrix) - 1)
        for i in range(1, len(matrix)):
            for k in range(i+1):
                sum = matrix[i-k][0] + matrix[k][1]
                if (sum > s_max):
                    s_max = sum
                    path[i-1] = str(i-k) + " " + str(k)

            profit_matrix_copy[i-1][j+1] = s_max
        path_matrix.append(path)

    distribution = []
    i = -1
    if len(path_matrix):
        path = path_matrix[i][-1].split()
        distribution.append(int(path[1]))
        while -i != len(path_matrix)+1:
            i -= 1
            if -i == len(path_matrix) + 1:
                distribution.append(int(path[0]))
            elif int(path[0]) != 0:
                path = path_matrix[i][int(path[0])-1].split()
                distribution.append(int(path[1]))
            else:
                distribution.append(0)
        distribution.reverse()
    else:
        distribution.append(1)

    return {
        PROFIT: profit_matrix_copy[-1][-1],
        DISTRIBUTION: distribution
    }


def is_error(profit_matrix: list[list[int]]):
    if profit_matrix is None or profit_matrix == [] or profit_matrix == [[]]:
        raise ValueError(PARAM_ERR_MSG)

    if not profit_matrix:
        raise ValueError(PARAM_ERR_MSG)

    if profit_matrix == [[]]:
        raise ValueError(PARAM_ERR_MSG)

    first_row_len = len(profit_matrix[0])
    for row in profit_matrix:
        # Проверка на то, что в матрице нет строк разной длины
        if len(row) != first_row_len:
            raise ValueError(PARAM_ERR_MSG)
        for item in row:
            # Проверка на то, что в матрице только тип float и int
            if not isinstance(item, int) and not isinstance(item, float):
                raise ValueError(PARAM_ERR_MSG)
        for item in row:
            # Проверка на то, что в матрице нет отрицательных значений
            if item < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG)


def main():
    profit_matrix = [[5, 7, 2, 10],
                  [9, 8, 4, 15],
                  [11, 10, 5, 16],
                  [12, 12, 8, 17],
                  [14, 15, 9, 18]]

    # profit_matrix = [[1]]
    print(get_invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
